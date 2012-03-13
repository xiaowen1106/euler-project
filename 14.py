def next(x):
	if x%2 == 0:
		return x/2
	else:
		return 3*x + 1

def getLength(start):
	current = start
	seq = [start]
	while True:
		current = next(current)
		seq.append(current)
		if current == 1:
			return len(seq)

length = 1
answer = 1

for i in range(1, 1000001):
	currentLength = getLength(i)
	if currentLength > length:
		length = currentLength
		answer = i

print answer
print length

