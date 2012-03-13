def factors(number):
	facs = [1]
	for i in range(2, number):
		if number%i == 0:
			facs.append(i)
	return sum(facs)

answer = 0
for i in range(2,10000):
	d = factors(i)
	if factors(d) == i and not d == i:
		print i,d
		answer += i

print answer
