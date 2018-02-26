def main():
    length = int(input())
    digits = input()
    limit = int(digits.replace(' ', '9'))
    print(magic_square(digits, limit, length))


def magic_square(digits: str, limit: int, length: int) -> int:
    i = 1

    while i * i < limit:
        square = i * i
        if matches_pattern(digits, str(square), length):
            return i
        else:
            i += 1


def matches_pattern(base: str, compare: str, length: int) -> bool:
    if len(base) != len(compare):
        return False
    for i in range(0, length * 2, 2):
        if base[i] != compare[i]:
            return False

    return True


if __name__ == '__main__':
    main()
