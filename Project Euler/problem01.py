
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    threes = 0
    fives = 0
    fifteens = 0

    if n % 3 == 0:
        threes = (n - 1) // 3
    else:
        threes = n // 3

    if n % 5 == 0:
        fives = (n - 1) // 5
    else:
        fives = n // 5

    if n % 15 == 0:
        fifteens = (n - 1) // 15
    else:
        fifteens = n // 15

    sum3 = (3 * threes * (threes + 1)) // 2
    sum5 = (5 * fives * (fives + 1)) // 2
    sum15 = (15 * fifteens * (fifteens + 1)) // 2

    print(sum3 + sum5 - sum15)

