import sys
from math import ceil
from datetime import datetime
starttime = datetime.now()

class Memoize:
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
        
def proper_divisors(x):
	divisors = [1]
	for i in range(2, x):
		if (x % i) == 0:
			if i not in divisors:
				divisors.append(i)
			if x/i not in divisors:
				divisors.append(int(x/i))
	return divisors

abundants = []
def generate_abundants(limit):
	for i in range(12, limit+1):
		if (sum(proper_divisors(i)) > i):
			abundants.append(i);
	
def can_be_written_as_sum_of_two_abundants(value):
	
	pass

proper_divisors = Memoize(proper_divisors);

#This is the smallest number that can be written as the sum of two abundant numbers
start = 24
#Anything above this can be written as the sum of two abundant numbers
limit = int(sys.argv[1]) #28123

generate_abundants(limit);

values = list(range(1,start))
for i in range(start, limit):
	if (can_be_written_as_sum_of_two_abundants(i)) is False:
		values.append(i)

print("Sum:      ", sum(values))
print("Abundants:", abundants)
print(len(abundants))
print(datetime.now()-starttime)

