#!/bin/python3

# https://www.hackerrank.com/challenges/simple-array-sum/problem

import os
import sys
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    
    sum = 0
    for i in range(len(ar)):
        sum = sum + ar[i]
    return sum
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))


    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
