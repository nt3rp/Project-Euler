import sys
from utils.math import gcd

def main():
    """What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?"""
    lcm = 1

    for i in range(lcm+1, 21):
        lcm = (lcm * i) / (gcd(lcm, i))

    print lcm

if __name__ == '__main__':
    sys.exit(main())
