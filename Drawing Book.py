#!/bin/python3
# https://www.hackerrank.com/challenges/drawing-book/problem
import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    if p%2 ==0:
        c1 = p /2
        c2 = (n-p)/2

    else:
        c1 = (p-1)/2
        c2 = (n - p -1)/2

    if c1<=c2:
        return(int(c1))
    else:
        return(int(c2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
