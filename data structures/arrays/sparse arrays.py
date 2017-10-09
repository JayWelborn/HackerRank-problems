strings = []

# input == N == number of strings
for i in range(int(input())):
    strings.append(input())

# input == Q == number of queries
for i in range(int(input())):
    print(strings.count(input()))