#!/usr/bin/env python3
"""Decrypt a message reversing chall.py (script below):


import string
from secret import MSG


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)


ct = encryption(MSG)
f = open("./msg.enc", "w")
f.write(ct.hex())
f.close()

"""


def decrypt(msg):
    "decrypt a message by reversing the operations in chall.py"
    c = []
    for char in msg:
        char = char - 18
        char = 179 * char % 256
        c.append(char)
    return bytes(c)


with open("msg.enc", encoding="utf-8") as f:
    ct = bytes.fromhex(f.read())
    cd = decrypt(ct)
    print(cd)
