#!/bin/python3
import os

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    length = len(ar)
    divs = 0
    for i in range(length):
        for j in range(i+1, length):
            if (ar[i] + ar[j]) % k == 0:
                divs += 1
    return divs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
