#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    from collections import Counter
    c = Counter(a) -Counter(b)
    d = Counter(b) -Counter(a)

    return(sum(c.values()) + sum(d.values()))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
