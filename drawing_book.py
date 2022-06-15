#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    pages_s = 0
    pages_e = 0
    i = 0
    while i != p and i + 1 != p:
        pages_s += 1
        i += 2

    if n % 2 == 0: n += 1

    while n != p and n - 1 != p:
        pages_e += 1
        n -= 2

    return min(pages_s, pages_e)

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)