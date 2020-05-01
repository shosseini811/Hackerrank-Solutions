#!/bin/python3

#https://www.hackerrank.com/challenges/apple-and-orange/submissions/code/156240559

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(len(apples)):
        apples[i]+=a
    
    for j in range(len(oranges)):
        oranges[j]+=b

    counter1 =0
    counter2 =0

    for p in range(len(apples)):
        if (apples[p]-s>=0) and (t - apples[p]>=0):
            counter1 +=1

    for q in range(len(oranges)):
        if (oranges[q]-s>=0) and (t - oranges[q]>=0):
            counter2 +=1   
    
    print(counter1)
    print(counter2)



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
