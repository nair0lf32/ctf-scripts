"""A l'envers"""
import socket
import re

HOST = 'localhost'
PORT = 4000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if "Congratulations" in data:
            print(data)
            break
        word = re.findall(r'(\w+)', data)[0]
        print(data)
        print(word)
        solution = word[::-1]
        print(solution)
        s.send(solution.encode("utf-8")+b'\n')
        response = s.recv(1024).decode()
        print(response)
