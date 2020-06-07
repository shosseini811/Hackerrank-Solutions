#!/bin/python3
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):

    count=[]
    for i in range(p,q+1):
    
        d = int(math.log10(i)) + 1
        s= i*i
        r = s%(10**d)
        l = s//(10**d)
    
        if r + l==i:
            count.append(i)

    if len(count)!=0:

        print(*count, sep =' ')
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
