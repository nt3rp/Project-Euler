#Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000)

#Naive way: calculate it all out
arr = [ x**x for x in range(1,1001)]
#print arr
result = str(reduce(lambda x,y: x+y, arr))
print result[-10:]

#Smart way: after 8^8, we already have 10 digits. From here on, we just need to find the pattern of the remaining digits?
