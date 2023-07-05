#!/usr/env/python3
from pwn import * # you can also use requests
import re

host = "7c77fa5239520456.247ctf.com" 
port = 50325
conn = remote(host,port)

#first I want to print the intro lines because why not?
for i in range(3):
	res = conn.recvline()
	print(res)

# then I define my function to answer each line
def answer(res):
	nums = re.findall(r'\d+',res.decode("utf-8")) # God, I hate regexes
	nsum = int(nums[-2]) + int(nums[-1])
	print(nsum)
	data = str(nsum) + '\r\n'  # the whole challenge was about this: How to fcking endline correctly!!
	conn.send(data)
	res = conn.recvline()
	print(res)

# first call
answer(res)
	
#then for every line it's rinse and repeat
for i in range(499): # there are 500 operations to solve and I already solved one
	res = conn.recvline()
	print(res)
	answer(res)

# This runs for a bit and the last line is your flag!
res = conn.recvline()
flag = res.decode("utf-8")
print("FLAG: " + flag)

