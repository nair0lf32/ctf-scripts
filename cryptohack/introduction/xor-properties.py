#!/usr/bin/env python3
"""xor properties"""

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xor_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY3_xor_KEY2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY1 = bytes.fromhex(KEY1)
print("KEY1:", KEY1.hex())

KEY2_xor_KEY1 = bytes.fromhex(KEY2_xor_KEY1)
KEY2 = bytes([KEY1[i] ^ KEY2_xor_KEY1[i] for i in range(len(KEY1))])
print("KEY2:", KEY2.hex())

KEY3_xor_KEY2 = bytes.fromhex(KEY3_xor_KEY2)
KEY3 = bytes([KEY2[i] ^ KEY3_xor_KEY2[i] for i in range(len(KEY2))])
print("KEY3:",KEY3.hex())

FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = bytes.fromhex(FLAG_xor_KEY1_xor_KEY3_xor_KEY2)
FLAG = bytes([KEY1[i] ^ KEY2[i] ^ KEY3[i] ^ FLAG_xor_KEY1_xor_KEY3_xor_KEY2[i] for i in range(len(KEY1))])
print("FLAG:",FLAG.decode())
