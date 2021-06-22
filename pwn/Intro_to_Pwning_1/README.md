## Task:
Execute the WINgardium_leviosa().

## Compiler flags:
checksec --file=pwn1
* ASLR enabled
* No stack canary

## Bugs:
* Format string vulnerability in printf() in welcome().
* Stack buffer overflow due to the use of gets() in AAAAAAAA() and welcome().

## Sub-task:
* Stack frame i.e. rsp needed to be 16B aligned and the 'rip' value that got overwritten was not in the muliple of 16.
* gets() breaks the input at the '\n' newline character and many 'ret' instructions had '\x0a' in their addresses.
* Input string should match with "Expelliarmus".

## Solution: 
* Found one 'ret' instruction inside deregister_tm_clones() that did not have '\x0a' in its address.
* Defeat ASLR by exploiting the format string vulnerability to read address stored in the stack. Read the address that belongs to the 'text' section.
* Use the leaked address to calculate the target function's starting address and 'ret' address in deregister_tm_clones().
* To align stack frame (rsp), first return to address that points to 'ret' before calling the address of target function. Hence, the '$extra_ret' was required.
* Final payload: "Expelliarmus\0AAAA....< address-to-ret-in-deregister_tm_clones > < address-to-start-of-WINgardium_leviosa >"

