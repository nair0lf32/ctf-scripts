#!/usr/bin/python
counter = 0
with open("data.dat") as f: 
	for line in f.readlines(): 
		if line.count('0') % 3 == 0 or line.count('1') % 2 == 0: 
			counter +=1
print(counter)
