n = int(input())
s = set(map(int, input().split())) 

num_cmds = int(input())
cmds = {
    'pop': set.pop,
    'remove': set.remove,
    'discard': set.discard
}

for _ in range(num_cmds):
    cmd = input().split(' ')
    if len(cmd) == 1:
        cmds[cmd[0]](s)
    else:
        cmds[cmd[0]](s, int(cmd[1]))

print(sum(s))
