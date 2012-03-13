import math

numbers = [0,1,2,3,4,5,6,7,8,9]
answer = []
final = 1000000 - 1

for i in range(10,0, -1):
	total = math.factorial(i)
	each = total / i
	start = int(final/each)
	answer.append(numbers[start])
	del numbers[start]
	final = final - each* start
print answer

