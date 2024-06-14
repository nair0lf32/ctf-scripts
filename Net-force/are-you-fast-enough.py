#!/usr/bin/python
"""Gotta go fast"""
import requests
import re
r = requests.get('https://www.net-force.nl/challenge/level602/prog2.php', timeout=3000)
number = int(re.findall(r'\d+', r.text)[0])
answer=(number * 3 + 2) - 250
r = requests.get(f'https://www.net-force.nl/challenge/level602/prog2.php?solution={answer}', timeout=3000)
print(r.text)
