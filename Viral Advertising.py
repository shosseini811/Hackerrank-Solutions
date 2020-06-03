#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked=2
    Cumulative=2
    shared =5

    if n==1: 
        return (2)
    else:
        for i in range(2, n+1):
            shared = liked *3
            liked = math.floor(shared/2)
            Cumulative = Cumulative + liked
    return(Cumulative)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
