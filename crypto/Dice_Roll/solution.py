#!/usr/bin/env python3
# flag{e915b62b2195d76bfddaac0160ed3194}
#python3 solution.py

from randcrack import RandCrack
from pwn import * 

def main():
	p = remote("challenge.nahamcon.com", 32535)
	#p = process("./dice_roll.py")

	print("Running...")
	rc = RandCrack()
	p.recvuntil("3. Guess the dice (test)")
	
	for i in range(624):
		p.sendline(b'2')    # payload sent as byte

		random_number = p.recvuntil("3. Guess the dice (test)") # return bytes
		random_number = random_number.decode().split('\n')
		random_number = int(random_number[3])

		rc.submit(random_number)    # submitting the generated random numbers

	p.sendline(b'3')
	p.recvuntil("Guess the dice roll to win a flag! What will the sum total be?")

	predicted_number = rc.predict_getrandbits(32)   # predicting the next number based on the 624 numbers submitted above
	p.sendline(str(predicted_number))   # payload sent as string
	print("predicted number:", predicted_number)

	flag = p.recvuntil("3. Guess the dice (test)") # return bytes
	flag = flag.decode().split('\n')[2]
	print(flag)

if __name__ == '__main__':
	main()
