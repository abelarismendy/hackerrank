#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour_24 = s[:-2]
    hour, minute, second = hour_24.split(':')
    hour = int(hour)
    if s[-2:] == "PM":
        if hour < 12:
            hour = hour + 12
        hour_24 = ':'.join([str(hour), minute, second])
    else:
        hour = hour%12
        hour_24 = ':'.join([f'{hour:02d}', minute, second])
    return hour_24

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
