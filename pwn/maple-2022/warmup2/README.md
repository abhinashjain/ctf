## Blocker:
* PIE, stack canary, NX bit  was enabled on the binary.

## Objective:
* Leak canary.
* Defeat binary's ASLR/PIE by leaking any binary address.
* Defeat libc's ASLR/PIE by leaking any libc address. (Use GOT/PLT table)
* Determine the libc version used. (Use LibcSearcher, libc-database online etc..) 
* Call libc's system() to get a shell.

## Solution: 
* vuln() function ask for input twice and the size of input read from stdio was sufficient to attack.
* Round 1: In first input, send the payload that will just overwrite the last byte (usually a NULL byte) of stack canary. Because puts() is used to print back the data in stdout, it will keep on printing untill it finds the NULL byte.
* Because we have overwritten the canary's NULL byte puts will print/leak the canary. We can now use this canary in our latter payloads.
* Round 1: In second input, use the above canary and then partial overwrite the stored rip address in the stack. Because PIE is enabled we can overwrite upto last 12 bits. 
* We chose to overwrite only the last 8 bits because in that way we can jump to "call vuln()" again call the vuln() to send future payloads.
* The 3rd last character of stored rip was different from the 3rd last character of vuln(), and was same as 3rd last character of 'call vuln'. Hence it made sense to use 'call vuln', otherwise we would have to brute forced the 3rd character in case we chose to jump directly to vuln().
* Round 2: In first input, send the payload until we reach rip address in stack. Because puts() is use to print back the data, we can leak stored rip value and use this leak address to bypass ASLR/PIE of binary.
* Use this leak address, subtract the offset (for that instruction, static value taken from objdump) to  determine the binary's base address.
* Calculate the runtime address of vuln(), "pop rdi; ret", and "ret" by adding their respective offsets (taken from objdump of binary) to the binary base address.
* And, then calculate the runtime address of GOT where address of read() and printf() are stored.
* Similarly, calculate the runtime address of PLT where code for lazy binding for puts() is stored. Although the address for puts() was already resolved before we will once again leverage the code in PLT to call puts() at runtime.
* Round 2: In second input, overwrite the canary (with value found above), put GOT address of read() and printf() in rdi, and call puts() to leak their runtime addresses. Hence defeating the ASLR/PIE of libc library.
* Use this leaked address to identify the libc version used in server. We can use LibcSearcher or libc-database to find the version.
* Use this leak address, subtract the offset (for that instruction/func, static value taken from libc's objdump or LibcSearcher also provides the .dump function to know the offset) to  determine the libc's base address.
* Once the libc's base address is known calculate the address of system() and "/bin/sh" by adding their respective offset to the libc's base address.
* Note: we need to use the correct libc version otherwise the offset will not match. Also, make sure the libc's base address always ends with 0x000, i.e. last 12 bits should be zero.
* Overwrite the rip with the vuln() address (calculated above).
* Round 3: In first input, send any bogus small data say "AAAAAA".
* Round 4: In second input, overwrite the canary (with value found above), put address of "/bin/sh" in rdi and jump to system() address and read the flag.

* Note: Do not use sendline() instead use send() pwntool function to prevent adding newline character at the time of partial overwrite.
