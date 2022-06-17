#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k = k%26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_may = alphabet.upper()
    to_rotate = alphabet[:k]
    new_alphabet = alphabet[k:] + to_rotate
    new_alphabet_may = new_alphabet.upper()
    alphabet = list(alphabet)
    alphabet_may = list(alphabet_may)
    new_alphabet = list(new_alphabet)
    new_alphabet_may = list(new_alphabet_may)

    new_s = ''

    for char in s:
        if char in alphabet:
            new_s += new_alphabet[alphabet.index(char)]

        elif char in alphabet_may:
            new_s += new_alphabet_may[alphabet_may.index(char)]

        else:
            new_s += char

    return new_s

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)