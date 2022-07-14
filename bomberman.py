import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# When bomb exploded, store 5 points on grid at set.
def afterBomb(r,c, grid, result):
    result.add((r,c))
    if r-1>=0:
        result.add((r-1,c))
    if c-1>=0:
        result.add((r,c-1))
    if r+1<len(grid):
        result.add((r+1,c))
    if c+1<len(grid[0]):
        result.add((r,c+1))

def bomberMan(n, grid):
    # Write your code here
    numrow = len(grid)
    numcol = len(grid[0])
    def explod(arr):
        afterbombSet = set()
        for r in range(numrow):
            for c in range(numcol):
                if arr[r][c] == "O":
                    afterBomb(r,c,arr,afterbombSet)
        result = []
        for i in range(numrow):
            tempStr = ''
            for j in range(numcol):
                if (i,j) in afterbombSet:
                    tempStr += '.'
                else:
                    tempStr += 'O'
            result.append(tempStr)
        return result
    if n==1:
        return grid
    if n%2==0:
        allBombs = ['O'*numcol for _ in range(numrow)]
        return allBombs
    else:
        if (n-1)%4==0:
            temp = explod(grid)
            return explod(temp)
        else:
            return explod(grid)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print(result)