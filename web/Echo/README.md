## Task:
Read flag.txt by injecting shell commands.

## Sub-task:
* Injected command should not be greater than 15 in length.
* Most of the generally used characters to execute commands are blacklisted. 

## Solution: 
* Use ` (backtick) to inject the command as it is not blacklisted.
* To bypass command length check, make use of already present 'echo' command to read the flag file.
* Final payload: http://example.com/?echo=`<../flag.txt` 
