#!/usr/bin/env python3
"""great common divisor"""

a = 66528
b = 52920

def find_gcd(a, b):
    """find the greatest common divisor of a and b
    doing this iteratively using Euclid's algorithm
    """
    while b:
        a, b = b, a % b
    return a

print(find_gcd(a, b))
