#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    people = [x for x in range(n)]
    return sum(people)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
