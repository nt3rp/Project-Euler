#Find the sum of the digits in the number 100!
from math import factorial

#Naive way; just use the sum function
value = str(factorial(100))
print sum(map(int,value))
