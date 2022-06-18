#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # arr.sort()
    # i = 0
    # unfair_min = float('inf')
    # while i <= len(arr)-k:
    #     sub = arr[i:i+k]
    #     unfair = max(sub)-min(sub)
    #     if unfair < unfair_min:
    #         unfair_min = unfair
    #     i += 1
    # return unfair_min
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))

if __name__ == '__main__':
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)