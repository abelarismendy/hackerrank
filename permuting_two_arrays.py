#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # A2 = A.copy()
    B2 = B.copy()
    for a in A:
        if a >= k:
            B2.remove(min(B2))
        else:
            diff = k - a
            candidatos = [x for x in B2 if x >= diff]
            if len(candidatos) == 0:
                return 'NO'
            B2.remove(min(candidatos))
    return 'YES'

if __name__ == '__main__':
    res = []

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        res.append(result)

    print(res)