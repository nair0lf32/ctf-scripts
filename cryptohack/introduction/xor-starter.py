#!/usr/bin/env python3
"""xor starter"""

str = "label"
key = 13

def xor(a, b):
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])

xor_flag = xor(str.encode(), key.to_bytes(1, byteorder='big'))
flag = "crypto{" + xor_flag.decode() + "}"
print(flag)
