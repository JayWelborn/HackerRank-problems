#!/bin/python3

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total_swaps = 0

while True:
    num_swaps = 0
    for i in range(1, len(a)):
        if a[i-1] > a [i]:
            b = a[i-1]
            a[i-1] = a[i]
            a[i] = b
            num_swaps += 1
            total_swaps += 1
    if num_swaps == 0:
        break
        
print("Array is sorted in {} swaps.".format(total_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))