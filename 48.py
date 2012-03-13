result = 0

for i in range(1, 1001):
	result += i**i

print result

answer = str(result)[-10:]

print answer
