primes = [2]
number = 2

def isPrime(number):
	for i in primes:
		if number%i == 0:
			return False
	return True



while True:
	number += 1
	if number >= 2000000:
		break
	if isPrime(number):
		primes.append(number)

print primes
print sum(primes)
