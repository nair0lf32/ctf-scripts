#!/usr/bin/env python3
"""base64 solution
Note to self: to avoid cyclic import error do not name this file base64.
as we are fricking importing base64 module here.
"""
import base64

flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_data = bytes.fromhex(flag)
base64_encoded = base64.b64encode(bytes_data)
decoded_string = base64_encoded.decode()
print(decoded_string)
