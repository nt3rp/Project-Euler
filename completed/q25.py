#What is the first term in the Fibonacci sequence to contain 1000 digits?

#Naive way: generate Fibonacci terms until the term is greater than 1000
a, b = 1, 1
count = 2
while len(str(b)) < 1000:
    count += 1
    a, b = b, a+b

print count
