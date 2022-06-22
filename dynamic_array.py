#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def binarizar(entero):
    binario = bin(entero)[2:]
    return binario


def xor(a,b):
    binario = ''
    diff = len(a) - len(b)
    if diff > 0:
        b = '0'*diff + b
    elif diff < 0:
        a = '0'*abs(diff) + a

    for i, bit1 in enumerate(a):
        bit2 = b[i]
        if bit1 != bit2:
            binario += '1'
        else:
            binario += '0'
    return int('0b'+binario, base=0)

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    ans = []
    for q in queries:
        a, x, y = q
        idx = ((xor(binarizar(x), binarizar(last_answer))) % n)
        if a == 1:
            arr[idx].append(y)
        elif a == 2:
            last_answer = arr[idx][y%len(arr[idx])]
            ans.append(last_answer)
    return ans


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    for r in result:
        print(str(r))