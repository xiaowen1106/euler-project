seq = [1, 2]
i = 0
answer = 2

while True:
	value = seq[i] + seq[i+1]
	i += 1
	seq.append(value)
	if value >= 4000000:
		break
	elif value%2 == 0:
		answer += value

print answer

