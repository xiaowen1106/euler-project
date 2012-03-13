number = 1

for i in range(1,11):
	number *= i

digits = str(number)
answer = 0

for d in digits:
	answer += int(d)

print answer
