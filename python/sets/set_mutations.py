input()
A = set(input().split())

methods = {
    'intersection_update': A.intersection_update,
    'update': A.update,
    'difference_update': A.difference_update,
    'symmetric_difference_update': A.symmetric_difference_update,
}

iterations = int(input())
for _ in range(iterations):
    methods[input().split()[0]](input().split())
    
print(sum([int(x) for x in A]))
