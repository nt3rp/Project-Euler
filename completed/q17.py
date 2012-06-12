#If all the numbers from 1 to 1000 (one thousand) inclusive
#were written out in words, how many letters would be used?
limit = 1000
start = 1

#with a simple modification, we could actually
#print them all out with their names
tens_count = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
ones_count = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] #include the odd case of teens

total = 0
for i in range(start, limit+1):
	thousands = ones_count[int(i / 1000)]
	if thousands > 0:
		thousands += 8 #thousand = 8
		
	hundreds = ones_count[int((i % 1000) / 100)]
	if hundreds > 0:
		hundreds += 7 # hundred = 7
		
	if (i % 100) < 20:
		tens = ones_count[i % 20]
	else:
		tens = tens_count[int((i % 100) / 10)] + ones_count[i % 10]	
	if hundreds > 0 and tens > 0:
		tens += 3 # and
		
	total += thousands + hundreds + tens
	
print(total)
