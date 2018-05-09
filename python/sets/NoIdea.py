input()

n = input().split(' ')
a = set(input().split(' '))
b = set(input().split(' '))

happiness = 0
for x in n:
    if x in a:
        happiness += 1
    if x in b:
        happiness -= 1
print(happiness)
