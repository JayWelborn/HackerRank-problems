def isBalanced(s):
    # Complete this function
    opening = '([{'
    stack = []

    for c in s:
        if (not stack) or (c in opening):
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'NO'
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 'NO'
    if not stack:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
