"""HackerRank Project Euler+ Problem #3.

This finds the largest prime factor of a given number (n).
"""


def main():
    t = int(input())
    for a0 in range(t):
        n = int(input())
        print(prime_factor(n))


def prime_factor(x):
    """Finds largest prime factor of x

    ::param:: int x
    ::return:: largest prime factor of x
    """

    # Begin by reducing even numbers as much as possible
    while x % 2 == 0:
        x = x // 2

    # Start checking factors at 2
    lpf = 2

    # Only check up to square root of x
    while (lpf * lpf <= x):

        # If x is evenly divisible by lpf, divide x by lpf
        if (x % lpf == 0):
            x = x // lpf
            # reset lpf for iteration
            lpf = 2

        # Increment lpf to 3 if it's 2, else to next odd number
        elif lpf == 2:
            lpf += 1
        else:
            lpf += 2

    # After dividing x by all possible numbers,
    # have the largest prime factor
    return x


if __name__ == '__main__':
    main()
