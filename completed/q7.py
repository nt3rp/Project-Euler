import sys

def main():
    """What is the 10001^(st) prime number?"""
	
    primes = [2]
    isPrime = True
    i = 3

    while len(primes) < 10001:
        for j in primes:
            if (i % j) == 0:
                isPrime = False
                break
        if (isPrime == True):
            primes.append(i)

        isPrime = True
        i += 1

    print primes.pop()

if __name__ == '__main__':
    sys.exit(main())	
