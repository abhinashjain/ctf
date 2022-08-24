## Compiler flags:
checksec --file=pwn2
* Arch:     amd64-64-little
* RELRO:    Partial RELRO
* Stack:    No canary found
* NX:       NX enabled
* PIE:      No PIE (0x400000)

## Solution: 
* Goal is to make value of 'key' as '/bin/sh' and then invoke 'system' call code that was already present inside the 'main' function at address 0x40072d.
* Since PIE is disabled, the address of code and data section will never change.
* Since it's 64bit binary, we have to pass argument of 'useme' function in register. Hence pop rdi and rsi gadgets were used.
* Value inside rdi and rsi are such that their muliplication will give the value as '/bin/sh' and stored in 'key' variable in data section.
* Make rdi point to the address of variable 'key' where the /bin/sh is stored and then 'call system' gadget present inside 'main' function.
* Align the stack by calling extra 'ret' instruction.
