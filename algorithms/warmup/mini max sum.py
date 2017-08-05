from itertools import combinations

arr = list(map(int, input().strip().split(' ')))

subsets = combinations(arr, 4)
min_sum = sum(arr)
max_sum = 0

for x in list(subsets):
    y = sum(x)
    if y > max_sum:
        max_sum = y
    if y < min_sum:
        min_sum = y

    
print('{} {}'.format(min_sum, max_sum))