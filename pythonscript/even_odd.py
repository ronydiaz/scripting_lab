#!/usr/bin/env python3

import sys

def even_odd(number):

    if number %2 == 0:
        print(f"The number {number} is even (module method)")
    else:
        print(f"The number {number} is odd (module method)")

    if number&1 != 0:
        print(f"The number {number} is odd (bitwice method)")
    else:
        print(f"The number {number} is even (bitwice method)")


even_odd(int(sys.argv[1]))
