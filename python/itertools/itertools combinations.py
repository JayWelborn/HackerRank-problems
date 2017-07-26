from itertools import combinations

prompt = input().split(' ')
string = prompt[0]
num = int(prompt[1])

for i in range(1, num+1):
    substrs = list(combinations(string, i))
    substrs = sorted([sorted(list(x)) for x in substrs])
    [print(''.join(x)) for x in substrs]