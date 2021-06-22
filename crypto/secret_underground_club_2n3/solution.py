#!/usr/bin/env python3
# CSCG{it_seems_like_somone_paid_attention_in_math_class}
# CSCG{even_a_blind_hen_sometimes_finds_a_grain_of_corn}
# python3 solution.py

def main():
    n_decimal = int(input("n from problem:"), 16)   #part of both public and private key
    plain_decimal = int(input("challenge that needs to be encrypted (in hex format): "), 16)
    
    plain = plain_decimal + n_decimal # Adding n to plain text to bypass the 'if' check in chat(), this bypass work because of (x^y)%z == ((x+z)^y)%z. x being the plain text
    
    plain_hex = hex(plain).split('x')[-1]
    print("\nplain text message: ", plain_hex)


if __name__ == '__main__':
    main()

