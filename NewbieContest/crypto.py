#!/usr/bin/python3
import requests

chall_url = "https://www.newbiecontest.org/epreuves/prog/prog5.php"
ans_url = "https://www.newbiecontest.org/epreuves/prog/verifpr5.php?solution="


# Reinventing the emperor's wheel
def decipher(encrypted, shift):
    start = ord("a")
    decrypted = ""
    for char in encrypted:
        decrypted += chr(((ord(char) - start - shift) % 26) + start)
    return decrypted


with requests.Session() as s:
    myCookies = {"MY-PRECIOUS-COOKIES"}

    chall = s.get(chall_url, cookies=myCookies)
    exp = chall.content.decode("ascii").split(" ")
    crypt = exp[6].replace("'", "")
    key = int(exp[-1].replace("'", ""))
    print("crypted: ", crypt, " key: ", key)
    solution = decipher(crypt, key)  # MINUSKEY
    print("decoded: ", solution)
    print(s.get(ans_url + str(solution), cookies=myCookies).text)
