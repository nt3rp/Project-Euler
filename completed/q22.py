#Using names.txt, a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order.
#Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

#What is the total of all the name scores in the file?
from functools import reduce

file = open('names.txt')
file_text = file.readline()
file.close()

#cleanup data
lines = file_text.split(",")
lines = [x.split("\"")[1] for x in lines]
lines.sort()

def maybe_ord(x):
	try:
		return ord(x)-64
	except:
		return x

def calculate_score(index, value):
	#char_sum = reduce(lambda x: print(x), value)
	char_sum = reduce(lambda x,y: maybe_ord(x) + maybe_ord(y), value)
	print (value, index, char_sum)
	return index * char_sum

total = 0
for i, value in enumerate(lines):
	total += calculate_score(i+1, value)

print(total)
