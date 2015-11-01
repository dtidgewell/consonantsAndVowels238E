import random
import sys
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
x = 1
while (x==1):
	pattern = raw_input('Enter pattern: ')
	x = 0
	for i in pattern:
		if i not in ['c', 'C', 'v', 'V']:
			x=1
	if(x==1): print('Input can only consists of c, C, v, and V')
for i in pattern:
	if(i == 'c'): sys.stdout.write(consonants[random.randint(0,20)])
	if(i == 'C'): sys.stdout.write(consonants[random.randint(0,20)].upper())
	if(i == 'v'): sys.stdout.write(vowels[random.randint(0,4)])
	if(i == 'V'): sys.stdout.write(vowels[random.randint(0,4)].upper())
print