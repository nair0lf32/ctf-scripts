#!/usr/bin/env python3
"""TCP - La roue romaine"""
import socket
import re
import codecs

HOST = "challenge01.root-me.org"
PORT = 52021
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode())
    # "Look behind and look ahead" regex
    encoded = re.findall(r"(?<=')(.*)(?=')", data.decode())[0]
    decoded = codecs.decode(encoded, "rot_13")
    s.sendall(decoded.encode())
    s.sendall(b"\n")
    response = s.recv(1024)
    print(response.decode())
