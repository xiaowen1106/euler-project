import math

flag = 0

for i in range(1,1001):
	for j in range(1,1001):
		k = math.sqrt(i*i + j*j) 
		if k%1 == 0 and i+j+k == 1000:
			a = i
			b = j
			c = k
			flag = 1
			break
	if flag == 1:
		break

print a,b,c,a*b*c
