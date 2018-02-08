def super_reduced_string(s):
    s = list(s)
    i = 1
    while i < len(s):
        if s[i - 1] == s[i]:
            s = s[0: i - 1] + s[i + 1:len(s)]
            i = 0
        i += 1

    if s:
        return ''.join(s)
    else:
        return "Empty String"


if __name__ == "__main__":
    s = input().strip()
    result = super_reduced_string(s)
    print(result)
