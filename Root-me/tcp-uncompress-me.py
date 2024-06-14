#!/usr/bin/env python3
"""TCP - Uncompress me"""
import socket
import re
import base64
import zlib

HOST = "challenge01.root-me.org"
PORT = 52022

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    response = s.recv(1024)
    while not "flag" in response.decode():
        print(response.decode())
        # "Look behind and look ahead" regex
        encoded = re.findall(r"(?<=')(.*)(?=')", response.decode())[0]
        base = base64.b64decode(encoded)
        decoded = zlib.decompress(base).decode()
        print(decoded)
        s.sendall(decoded.encode())
        s.sendall(b"\n")
        response = s.recv(1024)
        print(response.decode())
