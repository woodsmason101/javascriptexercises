import sys
while True:
	while True:
		print('Enter your email: ')
		email=input()
		space=print()
		if '@' not in email:
			print('no @ symbol\n try again')
			break
		if '.' not in email:
			print('no period\ntry again')
		else:
			print('email is valid')
			sys.exit()
