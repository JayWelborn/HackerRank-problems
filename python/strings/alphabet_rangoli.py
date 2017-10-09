# Hackerrank problem https://www.hackerrank.com/challenges/alphabet-rangoli


def print_rangoli(size):
    """
    Print a rangoli of given size composed of alphabet letters. Should match
    examples at https://www.hackerrank.com/challenges/alphabet-rangoli
    """
    from string import ascii_lowercase
    substring = ascii_lowercase[:size]
    print(substring)


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
