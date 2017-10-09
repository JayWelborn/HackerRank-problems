# Hackerrank problem https://www.hackerrank.com/challenges/alphabet-rangoli


def print_rangoli(size):
    """
    Print a rangoli of given size composed of alphabet letters. Should match
    examples at https://www.hackerrank.com/challenges/alphabet-rangoli
    """
    from string import ascii_lowercase
    letters = ascii_lowercase[:size][::-1]

    for i in range(1, size + 1):
        first_half = letters[:i]
        second_half = first_half[::-1][1:]
        rangoli_letters = '-'.join(first_half + second_half)
        width = size * 4 - 3
        print(rangoli_letters).center(width, '-')

    for i in range(size - 1, 0, -1):
        first_half = letters[:i]
        second_half = first_half[::-1][1:]
        rangoli_letters = '-'.join(first_half + second_half)
        width = size * 4 - 3
        print(rangoli_letters).center(width, '-')


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
