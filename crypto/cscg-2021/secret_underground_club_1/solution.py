#!/usr/bin/env python3
# https://simple.wikipedia.org/wiki/RSA_algorithm
# CSCG{rsa_seems_easy_but_apparently_it_is_not}
# python3 solution.py

def main():
    e_decimal = int(input("e from problem:"), 16)   #part of public key, use for decryption here
    n_decimal = int(input("n from problem:"), 16)   #part of both public and private key
    sig_cipher_decimal = int(input("signature or cipher text message that needs to be decrypted (in hex format): "), 16)

    plain = pow(sig_cipher_decimal, e_decimal, n_decimal)
    plain_hex = hex(plain).split('x')[-1]
    print("\nplain text message: ", plain_hex)


if __name__ == '__main__':
    main()
