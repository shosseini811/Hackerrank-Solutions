#!/bin/python3

# https://www.hackerrank.com/challenges/between-two-sets/submissions/code/156379761

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    counter =0
    c = list(range(a[n-1],b[0]+1))
    d=[]

    for i in c:
        for j in a:
            if i%j!=0:
                counter +=1
        
        for k in b:
            if k%i!=0:
                counter +=1
        
        if counter==0:
            d.append(i)
        counter =0
    
    return(len(d))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
