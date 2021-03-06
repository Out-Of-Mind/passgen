import sys
import random as r

lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spec_symbols = ['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','?','|',':',';']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = (lower_case, upper_case, nums, spec_symbols)

paswd = ''

def check(n):
	try:
		sys.argv[n]
		r = True
	except:
		r = False
	finally:
		return r

def generate(n, agr, paswd):
	for i in range(0, int(n)):
		if agr == 1:
			ra = r.randint(0, 2)
			paswd += str(symbols[ra][r.randint(0, len(symbols[ra])-1)])
		elif agr == 2:
			ra = r.randint(0, 3)
			paswd += str(symbols[ra][r.randint(0, len(symbols[ra])-1)])
		else:
			print('Wrong input')
			sys.exit(0)
	return paswd

chrs = 8
agr = 2

if check(1) and sys.argv[1] == '-p':
	pass_ = True
	if check(2):
		chrs = sys.argv[2]
		if check(3) and sys.argv[3] == '-lus':
			agr = 2
		elif check(3) and sys.argv[3] == '-lu':
			agr = 1
		else:
			arg = 1
		password = generate(int(chrs), agr, paswd)
else:
	n = input('Enter number of symbols: ')
	try:
		int(n)
	except:
		print('Isn\'t a number')
		sys.exit(0)
	agr = input('Please select 1 or 2:\n [1] lower case, upper case, numbers\n [2] lower case, upper case, numbers, special symbols\n')
	try:
		int(agr)
	except:
		print('Wrong input')
		sys.exit(0)
	password = generate(int(n), int(agr), paswd)

print(password)
