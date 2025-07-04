#!/usr/bin/env python3
"""xor starter"""

STR = "label"
KEY = 13


def xor(a, b):
    """XOR two byte sequences"""
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])


xor_flag = xor(STR.encode(), KEY.to_bytes(1, byteorder='big'))
FLAG = "crypto{" + xor_flag.decode() + "}"
print(FLAG)
