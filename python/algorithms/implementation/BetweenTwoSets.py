#!/bin/python3

import os
import sys
from math import sqrt, floor

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    possible = set()
    a.sort()
    b.sort()
    for i in range(1, b[0] + 1):
        factor = True
        for j in b:
            if j % i != 0:
                factor = False
        if factor:
            possible.add(i)
    
    remove = []
    for i in a:
        for j in possible:
            if j % i != 0:
                remove.append(j)
    for r in remove:
        if r in possible:
            possible.remove(r)
    
    return len(possible)
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    total = getTotalX(a, b)
    
    f.write(str(total) + '\n')

    f.close()
