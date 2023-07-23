#!/usr/bin/python
from pwn import *
import re

host = "7c77fa5239520456.247ctf.com" 
port = 50325
conn = remote(host,port)

for i in range(3):
	res = conn.recvline()
	print(res)

def answer(res):
	nums = re.findall(r'\d+',res.decode("utf-8"))
	nsum = int(nums[-2]) + int(nums[-1])
	print(nsum)
	data = str(nsum) + '\r\n'
	conn.send(data)
	res = conn.recvline()
	print(res)

# first call
answer(res)

for i in range(499): # there are 500 operations to solve and I already solved one
	res = conn.recvline()
	print(res)
	answer(res)

res = conn.recvline()
flag = str(res)

print("FLAG: " + flag)
