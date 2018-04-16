n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

sent = 1
num_swaps = 0
while (sent != 0):
    sent = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            num_swaps = num_swaps + 1
            a[i], a[i - 1] = a[i - 1], a[i]
            sent = 1
    
print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
