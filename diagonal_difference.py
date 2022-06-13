
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    n = len(arr)
    m = n-1
    for i in range(n):
        for j in range(n):
            if i == j:
                d1 += arr[i][j]

            if m == j:
                d2 += arr[i][m]
                m -= 1

    return abs(d1 - d2)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)