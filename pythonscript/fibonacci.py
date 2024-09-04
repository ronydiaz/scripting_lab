#!/usr/bin/env python3

import sys

print("Fibonacci function")

def fibonacci(n):
    secuence = [0,1]

    while len(secuence) < n:
        next_value = secuence[-1] + secuence[-2]
        secuence.append(next_value)
    
    return secuence

print(fibonacci(int(sys.argv[1])))
