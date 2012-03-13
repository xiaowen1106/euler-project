
def palin(text):
	for i in range(0, len(text)/2):
		if not text[i] == text[-i-1]:
			return False
	return True

answer = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		if palin(str(i*j)):
			if i*j > answer:
				answer = i*j

print answer
