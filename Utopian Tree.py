#!/bin/python3
# https://www.hackerrank.com/challenges/utopian-tree/problem
import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n==0:
        return(1)
    
    elif n%2 ==0:
        return(2**(n//2 + 1)  -1 )

    else:
        return(2**((n+1)//2 + 1)  -2 )




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
