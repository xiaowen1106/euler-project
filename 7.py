count = 1
primes = [2]
number = 2

def isPrime(number):
	for i in primes:
		if number%i == 0:
			return False
	return True



while True:
	number += 1
	if isPrime(number):
		count += 1
		primes.append(number)
	if count == 10001:
		print number
		break
