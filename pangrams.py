#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower().split(' ')
    s = list(''.join(s))
    s = set(s)
    if len(s) < 26:
        return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    s = input()

    result = pangrams(s)
    print(result)