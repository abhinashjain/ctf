## Task:
Encrypt the given plain text starting with 'challenge\_' using the provided chat() service

## Solution: 
* From problem.py take the value of n and challenge/plain text (through Login option) and pass them as input to solution.py.
* solution.py add both numbers. Take this output and pass in "Support" as a message/plain text.
* Take the generated signature/cipher text (after #) from "Support" and pass in "Login".

This works due to the modulus, the final modulus value i.e. signature/cipher text would be same whether generated as (x^y)%z or ((x+z)^y)%z. x being the plain text message.
When plain text represented as latter it helps in bypassing the check present in chat() function.
The generated signature/cipher text when decrytped will give same challenge/plain text value.

