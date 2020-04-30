#!/bin/python3

# https://www.hackerrank.com/challenges/compare-the-triplets/submissions/code/142542123

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    suma=0
    sumb=0
    for i in range(len(a)):
        if a[i]>b[i]:
            suma =suma + 1
        elif a[i]<b[i]:
            sumb = sumb + 1

    return (suma, sumb)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
