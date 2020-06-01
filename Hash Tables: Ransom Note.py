#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem


import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    c = 0


    for i in note:
        if i not in magazine:
            c+=1
            break
        else:
            magazine.remove(i)
    
    if c==0:
        print("Yes")
    else: 
        print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
