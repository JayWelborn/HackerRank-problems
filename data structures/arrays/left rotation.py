n,d = input().split(' ')
d = int(d)
arr = [int(x) for x in input().split(' ')]

[print(x, end=' ') for x in arr[d:] + arr[:d]]