#How many routes are there through a 20 x 20 grid?
from math import factorial 

routes = 0
k = 20
n = 2*k

#See the following for a HUGE tip!
#http://en.wikipedia.org/wiki/Pascal%27s_Triangle#Overall_patterns_and_properties

#until I find a choice function in python...
routes = factorial(n) / (factorial(k) * factorial(n-k))
print routes
