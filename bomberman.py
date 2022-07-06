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

def printMatrix(matrix):
    for i in matrix:
        print(i)
    print()

def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])
    if n % 2 == 0:
        # fill the grid with bombs
        grid = [['O' for i in range(cols)] for j in range(rows)]
        grid = [''.join(row) for row in grid]
        return grid
    if n % 3 == 0:

        for second in range(3):
            if second == 0:
                counter_grid = [[-1 if grid[i][j] == "." else 2 for j in range(cols)] for i in range(rows)]
                grid = [["." if grid[i][j] == "." else "O" for j in range(cols)] for i in range(rows)]
            else:
                detonate = []
                for i in range(len(counter_grid)):
                    for j, b in enumerate(counter_grid[i]):
                        if b == -1 and (i,j) not in detonate and second % 2 == 0:
                            counter_grid[i][j] = 2
                            grid[i][j] = "O"
                        elif b > 0:
                            b -= 1
                            counter_grid[i][j] = b
                            grid[i][j] = "O"
                        if b == 0:
                            counter_grid[i][j] = -1
                            grid[i][j] = "."
                            if i > 0:
                                counter_grid[i-1][j] = -1
                                grid[i-1][j] = "."
                            if j > 0:
                                counter_grid[i][j-1] = -1
                                grid[i][j-1] = "."
                            if i + 1 < rows and counter_grid[i+1][j] != 1:
                                grid[i+1][j] = "."
                                counter_grid[i+1][j] = -1
                                detonate.append((i+1, j))
                            if j + 1 < cols and counter_grid[i][j+1] != 1:
                                grid[i][j+1] = "."
                                counter_grid[i][j+1] = -1
                                detonate.append((i, j+1))
            # printMatrix(matrix=counter_grid)
            # printMatrix(matrix=grid)

        # convert grid to list of strings
        grid = [''.join(row) for row in grid]
    return grid

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