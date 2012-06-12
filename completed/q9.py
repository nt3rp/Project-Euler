#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which, a^2 + b^2 = c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc

def proper_sum(a, b, c):
	return ((a + b + c) == 1000)
	
def triplet(a, b, c):
	return (a >= 1) and (b >= 1) and (c >= 1) and ((a**2 + b**2) == c**2)
	
# BRUTE FORCE:
# fix one side length,  then try all possible lengths up to that side length
# ...cover all combinations
for i in range(1, 1001):
	for j in range(1, i+1):
		a = i
		b = i+j
		c = 1000 - ( a + b )
		if proper_sum(a, b, c) and triplet(a, b, c):
			print(a, b, c, a * b * c)
			quit()
		
	
