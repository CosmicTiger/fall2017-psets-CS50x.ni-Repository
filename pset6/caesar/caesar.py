from cs50 import get_int, get_string
import sys
import argparse

"""
    // Autor: Luisángel Martín Marcia Palma
    // PSET 6 caesar.py
"""

def caesarcypher(k):

    k = int(k)

    pt = get_string("plaintext:")
    counter = int(0)
    n = len(pt)
    print("ciphertext: ", end="")
    encription = ''
    for i in range(0, n, 1):
        c = ord(pt[i]) + k % 26
        if(pt[i].isalpha()):
            if(pt[i].isupper()):
                if(c > 90):
                  encription += chr(c - 26)
                else:
                     encription += chr(c)
            elif pt[i].islower():
                if(c > 122):
                    encription += chr(c - 26)
                else:
                    encription += chr(c)
        else:
            encription += pt[i]

    print(encription)
    return

def main():
    if sys.argv[1].isdigit() == False:
        raise Exception('Usage: ./caesar key')

    key = int(sys.argv[1])
    caesarcypher(key)
    return

if __name__ == '__main__':
    main()