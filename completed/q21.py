#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def proper_divisors(x):
	divisors = [1]
	for i in range(2, x):
		if (x % i) == 0:
			if i not in divisors:
				divisors.append(i)
			if x/i not in divisors:
				divisors.append(x/i)
	return divisors

def d(n): #sum of proper divisors
	divisors = proper_divisors(n)
	
	return sum(divisors)
	
#amicable pair iff d(a) = b, d(b) = a, a != b
limit = 10000
total = 0
pairs = []
for a in range(1, limit+1):
	#we can probably ignore some values mathematically, for now, brute force
	b = d(a)
	c = d(int(b))
	if  a == c and a != b:
		pairs.append((a, b))
		total += a + b

print(total/2, pairs) 
