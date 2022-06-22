#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    grid = [sorted(row) for row in grid]
    size = len(grid)
    for i in range(size):
        if i >= 1:
            for j in range(len(grid[i])):
                if grid[i][j] < grid[i-1][j]:
                    return 'NO'
    return 'YES'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
