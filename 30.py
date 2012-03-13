members = []

for i in range(0,10):
	members.append(i**5)
print members

answer = []

value = 0
while True:
	digits = str(value)
	powers = 0	
	for d in digits:
		powers += members[int(d)]
	if powers == value and not value == 1 and not value == 0:
		answer.append(value)
	value += 1
	if len(digits)*members[9] < int('1'+'0'*(len(digits)-1)):
		break

print sum(answer)
