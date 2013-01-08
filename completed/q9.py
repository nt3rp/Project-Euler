import sys

def main():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."""

    # Brute force solution; fix one side, try all possible lengths
    for i in xrange(1, 1001):
        for j in xrange(1, i+1):
            a = i
            b = i+j
            c = 1000 - (a + b)
            if ((a + b + c) == 1000) and ((a**2 + b**2) == c**2):
                print(a*b*c)
                quit()

if __name__ == '__main__':
    sys.exit(main())	
