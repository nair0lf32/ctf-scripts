#!/usr/bin/python
"""Simple programming challenge"""
COUNTER = 0
with open("data.dat", encoding="utf-8") as f:
    for line in f.readlines():
        if line.count("0") % 3 == 0 or line.count("1") % 2 == 0:
            COUNTER += 1
print(COUNTER)
