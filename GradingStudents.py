#!/bin/python3

#https://www.hackerrank.com/challenges/grading/submissions/code/156210191

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    #print(type(grades))
    result=[]
    for i in range(len(grades)):
        if grades[i]>37:
            if (grades[i]%5)<3:
                result.append(grades[i])
                
            else:
                result.append((int(grades[i]/5) +1)*5)
        else:
            result.append(grades[i])
    return result        
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
