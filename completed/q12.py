#What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt
from math import floor

def triangleNum(x):
    return sum(range(x+1))

#brute force: keep constructing larger triangle numbers until you have the proper number of divisors
count = 1
numDivisors = 0
limit = 500

while(True):
    numDivisors = 0
    num = triangleNum(count)
    for i in range(1,floor(sqrt(num))): #divisors come in pairs
        if(num % i == 0):
            numDivisors +=2
    if(numDivisors > limit):
        break
    count += 1
    
print num, count
