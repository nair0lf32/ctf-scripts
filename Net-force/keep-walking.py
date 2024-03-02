#!/usr/bin/python
"""keep walking"""
x=1
y=1
prev=1
answer = x * y + prev + 3

while x != 525:
    x += 1
    y += 1
    prev = answer
    answer = x * y + prev + 3

print(answer)
