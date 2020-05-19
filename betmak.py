#!/bin/python3
from argparse import ArgumentParser
from prettytable import PrettyTable


def solve(c1, c2, B):
    if not (1 / (c1 - 1) < c2 - 1):
        return 'Bad odds!'
    x2 = B * c1 / (c1 + c2)
    x1 = B - x2
    p = round(x1 * c1 - B, 2)
    x1, x2 = round(x1, 2), round(x2, 2)
    P = PrettyTable(['#', 'coefficient', 'bet', 'priel'])
    P.add_row([1, c1, x1, p])
    P.add_row([2, c2, x2, p])
    return P
    


parser = ArgumentParser(description='Mathematical deception of bookmakers')
parser.add_argument('c1', metavar='c1', help='coefficient for the first outcome',
                    type=float)
parser.add_argument('c2', metavar='c2', help='coefficient for the second outcome',
                    type=float)
parser.add_argument('-B', metavar='B', help='your budget', type=float, default=100)
args = parser.parse_args()

print(solve(args.c1, args.c2, args.B))
