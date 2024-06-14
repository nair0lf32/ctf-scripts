#!/usr/bin/python3
import requests  # I feel like using requests today

chall_url = "https://www.newbiecontest.org/epreuves/prog/prog1.php"
ans_url = "https://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution="

with requests.Session() as s:
    # ThiS IS THE CHALLENGE
    myCookies = {"PHPSESSID": "GET", "SMFCookie89": "YOUR OWN", "admin": "COOKIES"}

    chall = s.get(chall_url, cookies=myCookies)
    response = chall.text
    print(response)
    num = response.split(":")[-1].strip()
    print(s.get(ans_url + num, cookies=myCookies).text)
