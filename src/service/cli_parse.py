# -*- coding: utf-8 -*-

import argparse

print("+"*100)
print("The output things Before Main() function")

if __name__ == "__main__":
    print("*" * 50)
    print(" Enter main function ")

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

    print(" Leave main function ")
    print("=" * 50)


print("The output things After Main() function")
print("-"*100)
