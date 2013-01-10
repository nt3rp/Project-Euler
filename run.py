#!/usr/bin/env python
import argparse
import sys
import imp

def main():
    parser = argparse.ArgumentParser(description='Wrapper for Project Euler problems.')
    parser.add_argument('filename', metavar='FILE', help='Name of the file to run.')
    parser.add_argument('-q', dest='display_question', action='store_true', default=False, help='If present, displays the question.')
    parser.add_argument('-x', dest='no_output', action='store_true', default=False, help='If present, does not execute the question.')
    parser.add_argument('-t', dest='time_it', action='store_true', default=False, help='If prsent, measure the average execution time.')

    args = parser.parse_args()

    question = imp.load_source('question', args.filename)
    q_main = question.main

    if args.display_question:
        print q_main.__doc__

    if args.no_output:
        return

    print(q_main())

    if args.time_it:
        times = 1000 # How to set default, or value if flag present?
        print times

        from timeit import Timer
        t = Timer(lambda: q_main())
        print('{seconds} s to execute {number} times'.format(seconds=t.timeit(number=times),number=times))

if __name__ == "__main__":
    sys.exit(main())
