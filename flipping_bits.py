#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binario = bin(n)[2:]
    diff = 32-len(binario)
    if diff > 0:
        binario = f'{str(0)*diff}{binario}'
    binario = list(binario)
    for i in range(len(binario)):
        bit = binario[i]
        if bit == '1':
            binario[i] = 0
        else:
            binario[i] = 1

    exp = 0
    suma = 0
    for bit in reversed(binario):
        if bit == 1:
            suma += 2**exp
        exp += 1

    return suma
if __name__ == '__main__':
    q = int(input().strip())

    r = []

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        r.append(result)

    print(r)