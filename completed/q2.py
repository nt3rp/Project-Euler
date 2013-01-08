import sys

def main():
    """Find the sum of all the even-valued terms in the sequence which do not exceed four million."""
    total, a, b = 0, 1, 2
    while b < 4000000:
        a, b = b, a+b
        if ((a%2) == 0):
            total += a

    print total

if __name__ == '__main__':
    sys.exit(main())
