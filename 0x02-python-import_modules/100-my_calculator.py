#!/usr/bin/python3
import sys

from calculator_1 import add, sub, mul, div


if __name__ == '__main__':
    args = sys.argv
    cal = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # check if arguments is more than 3
    if len(args) > 4 or len(args) < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        if sys.argv[2] not in ['+', '-', '*', '/']:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            operator = sys.argv[2]
            b = int(sys.argv[3])
            print('{} {} {} = {}'.format(a, operator, b, cal[operator](a, b)))
