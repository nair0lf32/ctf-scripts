#!/usr/bin/python3
import requests
import math

chall_url = "https://www.newbiecontest.org/epreuves/prog/prog4.php"
ans_url = "https://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution="

with requests.Session() as s:
	myCookies = {"THESE COOKIES ARE MINE"} 

	chall = s.get(chall_url, cookies=myCookies)
	eq = chall.content.decode("ascii").split(" ")[0].strip()
	clean_eq = eq.replace('racine', 'math.sqrt').replace('&sup2;','**2')
	print(clean_eq)
	solution = eval(clean_eq) #Rare cases of eval usability
	print(int(solution))
	print(s.get(ans_url + str(solution), cookies=myCookies).text)
