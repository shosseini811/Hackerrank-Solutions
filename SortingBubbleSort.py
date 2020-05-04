#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    counter = 0
    for i in range(n):
        for j in range(n-1):
            if a[j]> a[j+1]:

                counter += 1
                temp=a[j+1]
                a[j+1] = a[j]
                a[j] = temp


    print ("Array is sorted in",  str(counter), 'swaps.',)
    print("First Element:", a[0])
    print("Last Element:", a[n-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
