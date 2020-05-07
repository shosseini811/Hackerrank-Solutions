#!/bin/python3

# https://www.hackerrank.com/challenges/mark-and-toys/problem
import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):

    prices.sort()
    sum = 0
    counter = 0
    for i in range(n):
        sum = sum +prices[i]
        counter +=1
        if sum==k:
            return counter
        elif sum>k:
            return (counter - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
