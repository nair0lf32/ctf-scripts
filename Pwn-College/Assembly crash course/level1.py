#!/usr/bin/python
"""set a register"""
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rdi, 0x1337
""" )
process = pwn.process("/challenge/run")
process.write(code)
response = process.readall()
print(response)
