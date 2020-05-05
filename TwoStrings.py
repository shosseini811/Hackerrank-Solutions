#!/bin/python3
#https://www.hackerrank.com/challenges/two-strings/problem

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
        for j in range(len(s1)):
            #for k in range(len(s2)):
                if s1[j] in s2:
                    return('YES')
                    #counter +=1
        return('NO')
                      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
