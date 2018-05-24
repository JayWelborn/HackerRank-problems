A = set(input().split())
n = int(input())
strict_superset = True
for _ in range(n):
    if not A.issuperset(set(input().split())):
        strict_superset = False
print(strict_superset)
