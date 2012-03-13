seq = [1,1]
count = 2

while True:
	current = seq[count-2]+ seq[count-1]
	count += 1
	if len(str(current))>999:
		print count		
		break
	else:
		seq.append(current)
