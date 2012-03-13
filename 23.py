import math

def factors(number):
	facs = [1]
	square = int(math.sqrt(number))
	for i in range(2, square+1):
		if number%i == 0:
			facs.append(i)
			if not i == number/i:
				facs.append(number/i)
	return sum(facs)

abundants = [12]

for i in range(13, 28113):
	if factors(i) > i:
		abundants.append(i)

array = range(25, 28125)

for i in abundants:
	for j in range(abundants[0],i+1):
		current = i+j
		if current in array:
			array.remove(current)

array.extend(range(1,24))

print sum(array)
		
