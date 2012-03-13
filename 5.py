answer = 1
factor = [1]

def divise(x):
	global factor
	for i in factor:
		if x%i == 0:
			x /= i
	return x

for i in range(1,21):
	if not answer%i == 0:
		answer *= divise(i)
		factor.append(divise(i))
		


print factor
print answer
