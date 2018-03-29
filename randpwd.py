#!/usr/bin/env python
"""
Simple generator of random passwords.
Generates a string alternating a consonant and a vowel, making the password
pronounceable.
"""

import sys
import random
import argparse

CONS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r',
        's', 't', 'v', 'w', 'x', 'y', 'z']
VOWELS = ['a', 'e', 'i', 'o', 'u']
PUNCT_MARKS = ['!', '#', '$', '%', '&', '/', '?', '*', ':', '.', '@', '+', '-', '_']
MAX_NUMERAL_LEN = 1000


def _random_int():
    return random.randint(0, sys.maxint)


def _random_next_bool():
    """True/False generated randomly"""
    return True if random.randint(0,1) == 1 else False


def generate_pwd(pwd_len, uppercase=True):
    done = False
    cons_size = len(CONS) - 1
    vowels_size = len(VOWELS) - 1
    p = ''
    i = 0

    while not done:
        # Random consonant
        c = CONS[random.randint(0, cons_size)]
        c = c.upper() if uppercase and _random_next_bool() else c
        p += c

        i += 1
        if i == pwd_len:
            done = True
            continue

        # Random vowel
        c = VOWELS[random.randint(0, vowels_size)]
        c = c.upper() if uppercase and _random_next_bool() else c
        p += c

        i += 1
        if i == pwd_len:
            done = True
            continue

    return p


def generate_combined_pwd(uppercase=True, numeral_size=99):
    len1 = 4 if _random_next_bool() else 3
    len2 = 3 if len1 == 4 else 4

    p1 = generate_pwd(len1, uppercase)
    p2 = generate_pwd(len2, uppercase)

    c = PUNCT_MARKS[random.randint(0, len(PUNCT_MARKS) - 1)]

    numerals = True if numeral_size > 0 else False
    n = str(random.randint(0, numeral_size)) if numerals else ''

    return "{}{}{}{}".format(p1, c, p2, n)


if __name__ == '__main__':
    ap_kwargs = {'description': 'Random Password Generator'}
    if (sys.version_info < (3,0)):
        kwargs['version'] = '1.0.1'
    parser = argparse.ArgumentParser(**ap_kwargs)
    parser.add_argument('number', type=int, action='store',
                        help='Number of passwords to be generated')
    parser.add_argument('--numeral-range', type=int, action='store',
                        help='Max value of the numeral part, between 0 and {}'.format(MAX_NUMERAL_LEN))
    args = parser.parse_args()

    if not (1 <= args.number <= 100):
        print('Valid values for number are 1 to 100')
        sys.exit(1)

    if args.numeral_range:
        if not (1 <= args.numeral_range <= MAX_NUMERAL_LEN):
            print('Valid values for the numeral part are 1 to {}'.format(MAX_NUMERAL_LEN))
            sys.exit(1)
        numeral_range = args.numeral_range
    else:
        numeral_range = 0

    for step in range(0, args.number):
        print(generate_combined_pwd(True, numeral_range))
