## Task:
Execute the WINgardium_leviosa().

## Compiler flags:
checksec --file=pwn2
* ASLR enabled
* Stack canary present

## Bugs:
* Format string vulnerability in printf() in welcome().
* Stack buffer overflow due to the use of gets() in AAAAAAAA() and welcome().

## Sub-task:
* Stack frame i.e. rsp needed to be 16B aligned and the 'rip' value that got overwritten was not in the muliple of 16.
* gets() breaks the input at the '\n' newline character and many 'ret' instructions had '\x0a' in their addresses.
* Input string should match with "Expelliarmus".
* Brute-force or leak the value of stack canary.

## Solution: 
* Found one 'ret' instruction inside deregister_tm_clones() that did not have '\x0a' in its address.
* Defeat ASLR by exploiting the format string vulnerability to read address stored in the stack. Read the stack canary and the address that belongs to the 'text' section.
* Use the leaked address to calculate the target function's starting address and 'ret' address in deregister_tm_clones().
* To align stack frame (rsp), first return to address that points to 'ret' before calling the address of target function. Hence, the '$extra_ret' is required.
* rbp comes in between the canary and rip. i.e. <canary> <rbp> <rip>. Hence, some garbage 8Bytes is pass after canary value.
* Final payload: "Expelliarmus\0AAAA....<leaked-stack-canary> AAAAAAAA < address-to-ret-in-deregister_tm_clones > < address-to-start-of-WINgardium_leviosa >"

