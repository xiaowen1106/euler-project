sumOfSquare = 0
sqaureOfSum = 0

for i in range(1,101):
	sumOfSquare += i*i
	sqaureOfSum += i
sqaureOfSum = sqaureOfSum*sqaureOfSum

print sqaureOfSum-sumOfSquare
