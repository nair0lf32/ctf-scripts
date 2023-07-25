#!/usr/bin/python3
import requests
import math

chall_url1 = "https://www.newbiecontest.org/epreuves/prog/prog3_1.php"
chall_url2 = "https://www.newbiecontest.org/epreuves/prog/prog3_2.php"
ans_url = "https://www.newbiecontest.org/epreuves/prog/verifpr3.php?solution="

with requests.Session() as s:
	myCookies = {"GETCHYOOWNCOOKIEEES"} 

	chall1 = s.get(chall_url1, cookies=myCookies)
	num1 = int(chall1.text.split(":")[-1].strip())
	chall2 = s.get(chall_url2, cookies=myCookies)
	num2 = int(chall2.text.split(":")[-1].strip())
	print(num1, " ", num2)
	solution = int(math.sqrt(num1) * num2)
	print(s.get(ans_url + str(solution), cookies=myCookies).text)
