n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary = []
secondary = []
for i in range(0, n):
    primary.append(a[i][i])
    secondary.append(a[n-i-1][i])
    
print(abs(sum(primary) - sum(secondary)))