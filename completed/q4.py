#Find the largest palindrome made from the product of two 3-digit numbers.
greatest = 0
for i in range(1000, 100, -1):
	for j in range(i, 100, -1):
		palindrome = str(j*i)
		if ((palindrome == palindrome[::-1]) and (j*i) > greatest):
			greatest = j*i
			
print greatest
