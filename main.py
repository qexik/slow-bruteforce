from string import digits, ascii_letters
from time import time

def get_next_password(local, cur):
	ind = len(cur) - 1
	last_letter = cur[ind]
	if cur[ind] != local[len(local) - 1]:
		last_letter = local[local.index(last_letter) + 1]
		return cur[0:ind] + last_letter
	else:
		for i in range(ind - 1, -1, -1):
			if cur[i] != local[len(local) - 1]:
				let = local[local.index(cur[i]) + 1]
				return cur[0:i] + let + local[0] * (ind - len(cur[0:i]))
	cur = local[0] * (len(cur) + 1)
	return cur

	
def generate(local, cur, counter):
	password = get_next_password(local, cur)
	counter += 1
	return (password, counter)
	
	
def guess_password(passw):
	local = digits + ascii_letters
	counter = 0
	t = time()
	start_pass = '0'
	password = start_pass
	while True:
		if password == passw:
			print('Пароль угадан за %d попыток. Ваш пароль - %s' % (counter, password))
			print(str(time() - t) + 'seconds.')
			break
		password, counter = generate(local, password, counter)

print('Enter your password:')
guess_password(input('>>'))
