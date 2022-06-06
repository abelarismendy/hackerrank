#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for number in arr:
        if number > 0:
            pos += 1
        elif number < 0:
            neg += 1
        elif number == 0:
            zero += 1
    pos = pos/total
    neg = neg/total
    zero = zero/total
    print(f'{pos:.6f}')
    print(f'{neg:.6f}')
    print(f'{zero:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
