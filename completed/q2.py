#Find the sum of all the even-valued terms in the sequence which do not exceed four million.
sum, a, b = 0, 1, 2
while b < 4000000:
	a, b = b, a+b
	print a, b
	if ((a%2) == 0):
		sum += a

print sum
