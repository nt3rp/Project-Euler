#What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
#from 1 to 20, find the unique primes
#primes = [2]
#isPrime = True

#for i in range(3,11):
#	for j in primes:
#		print i,j
#		if (i % j) == 0:
#			isPrime = False
#			break
#	if (isPrime == True):
#		primes.append(i)
#	isPrime = True

#lcm = 1

#for n in primes:
#	lcm *= n

#print lcm

def gcd(a,b):
	while b != 0:
		t = b
		b = a % b
		a = t
	return a

lcm = 1

for i in range(lcm+1,21):
	lcm = (lcm * i) / ( gcd(lcm,i) )
	
print lcm
