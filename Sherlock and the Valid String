#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    from collections import Counter
    a =Counter(s)
    b= Counter(a.values()).values()

    if len(b)>2:
        return "NO"

    elif len(b)==1:
        return "YES"

    elif len(b)==2:
        if min(b)>1:
            return "NO"
        else: 
            return "YES"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
