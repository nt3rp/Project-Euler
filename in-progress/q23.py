#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
#smallest number that can be written as the sum of two abundant numbers
#is 24. By mathematical analysis, it can be shown that all integers
#greater than 28123 can be written as the sum of two abundant numbers.
#However, this upper limit cannot be reduced any further by analysis
#even though it is known that the greatest number that cannot be
#expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written
#as the sum of two abundant numbers.
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

#This is the smallest number that can be written as the sum of two abundant numbers
start = 24
#Anything above this can be written as the sum of two abundant numbers
limit = int(sys.argv[1]) #28123

def proper_divisors(x):
	divisors = [1]
	for i in range(2, x):
		if (x % i) == 0:
			if i not in divisors:
				divisors.append(i)
			if x/i not in divisors:
				divisors.append(int(x/i))
	return divisors

proper_divisors = Memoize(proper_divisors);
		
def is_abundant(value):
	return sum(proper_divisors(value)) > value
	
def is_deficient(value):
	return sum(divisors) < value

def is_perfect(value):
	return sum(divisors) == value

is_abundant = Memoize(is_abundant)

#Too slow; need to execute this less times
def can_be_written_as_sum_of_two_abundants(value):
	for i in range(12, ceil(value/2)+1):
		a = proper_divisors(i);
		if is_abundant(i) is False:
			continue;
		b = proper_divisors(value-i)
		if is_abundant(value-i) is False:
			continue;
		if ((sum(a) + sum(b)) == value):
			return True
	return False

#def can_be_written_as_sum_of_two_abundants(value):
#	pass

values = list(range(1,start))
for i in range(start, limit):
	if (can_be_written_as_sum_of_two_abundants(i)) is False:
		values.append(i)

print(sum(values))
#print(proper_divisors.memo)
print(datetime.now()-starttime)
