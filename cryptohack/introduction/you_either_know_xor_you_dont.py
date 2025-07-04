#!/usr/bin/env python3
"""you either know xor you dont"""
from pwn import xor

FLAG = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded = bytes.fromhex(FLAG)
# we know the first bytes are "crypto{"
KEY = xor(decoded, "crypto{".encode())
# from output we try to guess the key
KEY = KEY[:7] + KEY[8:9]
# this is ugly but it works! might refactor later
print("key: ", KEY.decode())
print("flag: ", xor(decoded, KEY).decode())
