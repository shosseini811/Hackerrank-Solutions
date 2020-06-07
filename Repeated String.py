#!/bin/python3
# https://www.hackerrank.com/challenges/repeated-string/problem
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c=0
    p = s.count('a') * int(n/len(s))
    c = n - (math.floor(n/len(s)) * len(s))
    if c==0:
        return (p)
    else: 
        return( p + s[0:c].count('a'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
