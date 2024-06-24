#!/usr/bin/env python3
"""favorite byte"""

def byte_xor(ba1, ba2):
    """basically xor every single byte
    with another key byte in bytes array"""
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = bytes.fromhex(flag)

# Brute force the key
for c in range(256):
    key = bytes([c]*len(decoded))
    result = byte_xor(decoded, key)
    if b"crypto" in result:
        print(result)
        break
