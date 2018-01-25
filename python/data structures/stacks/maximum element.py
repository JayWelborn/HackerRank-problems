stack = []
elements = int(input())

for _ in range(elements):
    operation = [int(x) for x in input().split(' ')]
    if operation[0] == 1 and stack:
        stack.append(max(stack[-1], operation[1]))
    elif operation[0] == 1 and not stack:
        stack.append(operation[1])
    elif operation[0] == 2:
        stack.pop()
    else:
        print(stack[-1])

