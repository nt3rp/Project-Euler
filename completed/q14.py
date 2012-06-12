#The following iterative sequence is defined for the set of positive integers:
#n  n/2 (n is even)
#n  3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13  -> 40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
from math import log
#n = 1
#length = 1
#limit = 13

#def even_function (x):
#	return 2*x
	
#def odd_function (x):
#	return (x-1) / 3
	
#def odd_check (x):
#	return (x-1) % 3

#work from lowest number back to biggest?
#how do we know when to stop?

#want to maximize odd functions, as they reduce n
#while n < limit:
#	if (odd_check(n) == 0) and (odd_function(n) % 2 == 1) and (odd_function(n) > 1):
#		n = odd_function(n)
#	else:
#		n = even_function(n)
#	length += 1
#	print(n)

import sys
paths = []
limit = int(sys.argv[1])
n = 0
paths.append(0)

#Really dumb brute force method. Should have done a dynamic programming solution?
while n <= limit:
	#do steps for this path
	current_path = n
	paths.append(0)
	while current_path > 1:
		is_power_of_two = log(current_path, 2)
		if (is_power_of_two % 1) == 0:
			paths[n] += is_power_of_two
			break
		elif (current_path % 2) == 0:
			current_path /= 2
		else:
			current_path = 3 * current_path + 1
		paths[n] += 1
	n += 1

maxValue = max(paths);
maxIndex = paths.index(maxValue)
print(maxIndex, maxValue)
