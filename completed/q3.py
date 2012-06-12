#What is the largest prime factor of the number 600851475143 ?
from math import sqrt
from math import ceil

number = 600851475143
root = int(ceil(sqrt(number))) # this is the greatest possible prime factor of the number
for i in range(root, 2, -1):
	if( (number % i) == 0): 
		root = int(ceil(sqrt(i)))	
		prime = True
		for j in range(root, 2, -1):
			if( (i % j) == 0 ):
				prime = False
				break
		if (prime == True):
			print i
			quit()
				

