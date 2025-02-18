#!/bin/python3

import math
import os
import random
import re
import sys

sys.stdin = open("input/number_line_jumps1.txt","r")

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"

    while True:
        x1 += v1
        x2 += v2

        if x1 == x2:
            return "YES"

        if x1 > x2:
            return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])
    print(x1V1X2V2)

    result = kangaroo(x1, v1, x2, v2)

    # fptr.write(result + '\n')

    # fptr.close()
