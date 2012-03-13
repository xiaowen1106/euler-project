import math

i = 1
triangle = 0

def factors(number):
	facs = [1, number]
	square = int(math.sqrt(number))
	for i in range(2, square+1):
		if number%i == 0:
			facs.append(i)
			if not i == number/i:
				facs.append(number/i)
	return facs

while True:
	triangle += i
	facs = factors(triangle)
	if(len(facs)>500):
		print triangle
		print facs
		break
	i += 1
