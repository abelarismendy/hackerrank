#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # arr.sort()
    lo = 0
    hi = sum(arr)
    i = 1
    print()
    if len(arr) == 1 or hi == 0:
        return 'YES'
    hi -= arr[0]
    while i < len(arr):
        if lo == hi:
            return 'YES'
        lo += arr[i-1]
        hi -= arr[i]
        # print(i, lo, hi)
        # print(arr[i-1], arr[i])
        if lo == hi:
            return 'YES'
        i += 1
    return 'NO'


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
