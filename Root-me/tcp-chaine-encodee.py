#!/usr/bin/env python3
"""TCP - Chaîne encodée"""
import socket
import re
import base64

HOST = "challenge01.root-me.org"
PORT = 52023
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode())
    # "Look behind and look ahead" regex
    encoded = re.findall(r"(?<=')(.*)(?=')", data.decode())[0]
    decoded = base64.b64decode(encoded).decode()
    print(decoded)
    s.sendall(decoded.encode())
    s.sendall(b"\n")
    data = s.recv(1024)
    print(data.decode())
