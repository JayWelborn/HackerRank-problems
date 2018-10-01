#!/bin/python3

import os

# Complete the birthday function below.
def birthday(s, d, m):
    total = 0
    for i in range(len(s) - m + 1):
        sum = 0
        for j in range(0, m):
            sum += s[i + j]
        if sum == d:
            total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
