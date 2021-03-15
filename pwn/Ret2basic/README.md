## Task:
Execute the win().

## Compiler flags:
checksec --file=ret2basic
* ASLR disabled
* No stack canary

## Bugs:
* Stack buffer overflow due to the use of gets() in vuln().

## Solution: 
* Find the address of target function i.e. win() through gdb.
* Final payload: "AAAA....< address-to-start-of-win >"

