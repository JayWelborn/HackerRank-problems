from itertools import groupby

n = int(input().strip())

# get binary string
binary = '{0:b}'.format(n)

# use itertools groupby to get list of tuples
groups = groupby(binary)
results = [(label, sum(1 for _ in group)) for label, group in groups]

# iterate through list of tuples to get longest string of 1s
longest, current = 0, 0
for result in results:
    if result[0] == '1':
        current = result[1]
    else:
        longest = max(longest, current)
        current = 0
        
print(max(longest, current))
