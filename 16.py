import string
import math

def toLetters(x, l = 0):
	tableA = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tableB = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	if x < 20:
		return l + len(tableA[x])
	elif x < 100 and x >= 20:
		digits = str(x)
		return l + len(tableB[int(digits[0])-2]+tableA[int(digits[1])])
	elif x >= 100 and x < 1000:
		digits = str(x)
		if x%100 == 0:
			return len(tableA[int(digits[0])])+len('hundred')
		else:
			return toLetters(int(digits[1:]), len(tableA[int(digits[0])])+len('hundredand'))
	else:
		return len('onethousand')
		
answer = 0
for i in range(1,1001):
	print toLetters(i)
	answer += toLetters(i)

print answer
