import string

f = file('names.txt')
names = f.readline()
names = names.replace('"','').split(',')
names = sorted(names, key=str.lower)

dictionary = {}
j = 1
for s in string.ascii_letters:
	dictionary[s] = j
	j += 1

print dictionary

def value(word):
	global dictionary
	word = word.lower()
	value = 0
	for w in word:
		value += dictionary[w]
	return value
		

i = 1
answer = 0
for n in names:
	answer += i*value(n)
	i += 1

print answer
