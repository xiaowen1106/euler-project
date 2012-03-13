def isPrime(n):
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True
maximum = 0

for a in range(-1000,1001):
	for b in range(-1000,1001):
		n = 0
		while True:
			if n*n + a*n + b > 0 and isPrime(n*n + a*n + b):
				n += 1
			else:
				if n > maximum:
					maximum = n
					answer = [a,b]
				break
print answer[0]*answer[1]
