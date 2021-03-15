#!/usr/bin/env python3
#flag{06754e57e02b0c505149cd1055ba5e0b}
#python3 solution.py

import base64
import hashlib

def main():

    partkey = b"pgJ2K9PMJFHqzMnqEgL"
    cipher = "AA9VAhkGBwNWDQcCBwMJB1ZWVlZRVAENW1RSAwAEAVsDVlIAV00="
    cipher = base64.b64decode(cipher)   # return bytes, 38 Bytes
    
    for i in range(10000):
        salt = str(i).encode()  # convert to bytes
        
        key = hashlib.sha256()
        key.update(partkey)     # key
        key.update(salt)        # salt
        #key.update(partkey + salt)

        hashed = key.hexdigest()    # 32 Bytes, 64 hex char
        
        flag = ""
        # p = c XOR SHA256(key + salt). where each 4 bits (hex char) of SHA output is considered as 1B and XORed with 1B of cipher text
        for j in range(len(cipher)):
            flag += chr(cipher[j] ^ ord(hashed[j]));    # each hex char of hash value is considered as 1 Byte before XORing due to ord(). only 19 bytes (38 hex char) of hash value is used. 

        if "flag{" in flag:
            print(flag) # plain text
            break;

if __name__ == '__main__':
        main()


