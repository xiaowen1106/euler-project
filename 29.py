members = []

for a in range(2,101):
	for b in range(2,101):
		if not a**b in members:
			members.append(a**b)

print members
print len(members)
