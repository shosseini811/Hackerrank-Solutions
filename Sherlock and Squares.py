#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0

    for i in range(int(math.sqrt(a)),math.floor(math.sqrt(b+1))+1):

        if (i*i>=a) and (i*i<=b):
            count +=1 
    return (count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
