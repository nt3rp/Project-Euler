#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math

def sum(x):
	"""sum of the numbers 1 to x"""
	sum = 0
	for i in range(x+1):
		sum+=i
	return sum

def powsum(x, power):
	"""sum of the numbers 1^power to x^power"""
	sum = 0
	for i in range(x+1):
		sum+=math.pow(i,power)
	return sum

print math.pow(sum(100),2), powsum(100,2)
print math.pow(sum(100),2)-powsum(100,2)

