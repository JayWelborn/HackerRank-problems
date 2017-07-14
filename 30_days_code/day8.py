n = int(input())

phonebook = {}
for _ in range(n):
    entry = input()
    entry = entry.split(' ')
    phonebook[entry[0]] = entry[1]
    
while True:
    
    name = str(input())
    if name in phonebook:
        print('{}={}'.format(name, phonebook[name]))
        
    else:
        print('Not found')