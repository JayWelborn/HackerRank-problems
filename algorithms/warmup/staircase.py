n = int(input().strip())
spaces = n-1
hashes = 1

for _ in range(n):
    print(' '*spaces + '#'*hashes)
    spaces -= 1
    hashes += 1