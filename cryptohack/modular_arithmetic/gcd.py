#!/usr/bin/env python3
"""great common divisor"""

A = 66528
B = 52920


def find_gcd(n1, n2):
    """find the greatest common divisor of n1 and n2
    doing this iteratively using Euclid's algorithm
    """
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


print(find_gcd(A, B))
