#!/usr/bin/env python
import argparse
import sys
import imp

def main():
    parser = argparse.ArgumentParser(description='Wrapper for Project Euler problems.')
    parser.add_argument('filename', metavar='FILE', help='Name of the file to run.')
    parser.add_argument('-q', dest='display_question', action='store_true', default=False, help='If present, displays the question.')
    parser.add_argument('-x', dest='no_output', action='store_true', default=False, help='If present, does not execute the question.')

    args = parser.parse_args()

    question = imp.load_source('question', args.filename)
    q_main = question.main

    if args.display_question:
        print q_main.__doc__

    if not args.no_output:
        q_main()

if __name__ == "__main__":
    sys.exit(main())
