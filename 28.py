import math

diags = [1]

for i in range(1,1002,2):
	corner = i**2
	if not corner == 1:
		for j in range(0,4):
			diags.append(corner-(i-1)*j)

print sum(diags)
