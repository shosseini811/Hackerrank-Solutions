#!/bin/python3
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    l = []
    for q in range(i,j+1):
    
        sum = 0
        p=q
        while (p !=0):
            sum = sum*10 + p%10
            p = p//10
        l.append(sum)

    count =0
    for r,s in enumerate(range(i,j+1)):
        if ((s - l[r])%k)==0: 
            count +=1

    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
