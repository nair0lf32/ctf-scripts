#!/usr/bin/env python3
"""TCP - Retour au collège"""
import socket
import re
import math

HOST = "challenge01.root-me.org"
PORT = 52002
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode())
    nums = re.findall(r"\d+", data.decode())
    num1 = int(nums[1])
    num2 = int(nums[2])
    solution = round(math.sqrt(num1) * num2, 2)
    s.sendall(str(solution).encode())
    s.sendall(b"\n")
    response = s.recv(1024)
    print(response.decode())
