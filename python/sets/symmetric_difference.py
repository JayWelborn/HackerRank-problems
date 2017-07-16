a = int(input())

# make first set
M = set(map(int, input().split()))

b = int(input())

# make second set
N = set(map(int, input().split()))

# get difference
diff_1 = list(M.difference(N))
diff_2 = list(N.difference(M))
difference = diff_1 + diff_2

# print difference
[print(x) for x in sorted(difference)]