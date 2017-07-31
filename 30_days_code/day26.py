actual = [int(x) for x in input().split(' ')]
expected = [int(x) for x in input().split(' ')]

if actual[2] > expected[2]:
    print(10000)
elif actual[2] < expected[2]:
    print(0)
else:
    if actual[1] > expected[1]:
        print(500*(actual[1] - expected[1]))
    elif actual[1] < expected[1]:
        print(0)
    else:
        if actual[0] > expected[0]:
            print(15*(actual[0] - expected[0]))
        else:
            print(0)