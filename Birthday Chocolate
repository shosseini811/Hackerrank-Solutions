#!/bin/python3
# https://www.hackerrank.com/challenges/the-birthday-bar/problem
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):

    sum = 0
    counter = 0

    if m>n:
        return counter

    elif m==n:
        for i in range(m):
            sum += s[i]
        if sum == d:
            counter+=1
        return counter

    else:

        for j in range(n - m + 1):
            for i in range(m):
                sum += s[i + j]
            if sum == d:
                counter+=1
            sum = 0
        return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
