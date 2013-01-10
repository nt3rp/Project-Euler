import math

def main():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
    range_generator = xrange(101)
    square_of_sum  = math.pow(sum(range_generator), 2)
    sum_of_squares = sum((math.pow(x,2) for x in range_generator))
    return (square_of_sum - sum_of_squares)

if __name__ == '__main__':
    print(main())
