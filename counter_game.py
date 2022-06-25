import math
#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def recCounter(n, a):
    if n == 1:
        return a
    elif n & n-1 == 0:
        # print(n, 2)
        return recCounter(n//2, not a)
    else:
        power = 2**int(math.log2(n))
        # print(n-power, 0)
        return recCounter(n-power, not a)


def counterGame(n):
    res = recCounter(n, True)
    if res:
        return 'Richard'
    return 'Louise'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)
        print(result)
