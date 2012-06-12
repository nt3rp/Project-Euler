#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 1 + 1296 + 81 + 256
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#Notes
#1^5 =     1
#2^5 =    32
#3^5 =   243
#4^5 =  1024 
#5^5 =  3125
#6^5 =  7776
#7^5 = 16807
#8^5 = 32768
#9^5 = 59049

powers = [i**5 for i in range(10)]
results = [];
limit = 1000000 #how to set this effectively?

#brute force
for i in range(2, limit):
	list = [powers[int(i)] for i in str(i)]
	if (sum(list) == i):
		results.append(i);
		print(i, list)

print(sum(results))
