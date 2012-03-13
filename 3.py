value = 600851475143
answer = 1
i = 1

while True:
	if value % i == 0:
		answer = i
		value = value/i
		if value == 1:
			break
	i += 1

print answer
