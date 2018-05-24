reps = int(input())

for _ in range(reps):
    input()
    a = set(input().split())
    input()
    b = set(input().split())
    print(a.issubset(b))
