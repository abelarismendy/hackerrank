#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # total = 0
    # x = 0
    # while x <= n:
    #     if n + x == n ^ x:
    #         total += 1
    # return total

    if n == 0:
        return 1
    else:
        return pow(2, (str(bin(n)).count('0')-1))

if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)

    print(result)