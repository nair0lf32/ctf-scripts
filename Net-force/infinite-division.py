#!/usr/bin/python
"""Infinite division"""
from decimal import Decimal, getcontext
# why 5003 instead of 5000? Because the integer part has 3 digits, the presicion needs to be counted to 5003 digits. Took me a while to figure this out.
getcontext().prec = 5003
division = Decimal(13155187) / Decimal(13417)
print(division)
answer = str(division)[-6:]
print("solution: ", answer)
