#Find the sum of all the primes below two million.
from time import clock

value = 2000000
p = 2
primes = range(p,value)

start = clock()
#Using something like the sieve of eratosthenes
#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
while( (p*p) < value):
    i = primes.index(p)
    primes[i+1:] = filter(lambda x: x % p != 0, primes[i:])
    p = primes[i+1]
    
print primes[-1], sum(primes), clock() - start;

def main():
    """Find the sum of all the primes below two million."""
    # Using something like the sieve of eratosthenes
    # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    value = 2000000
    p = 2
    primes = range(p, value)

    while ((p*p) < value):
        i = primes.index(p)
        primes[i+1:] = filter(lambda x: x % p != 0, primes[i:])
        p = primes[i+1]

    return sum(primes)

if __name__ == '__main__':
    print(main())
