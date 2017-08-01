from random import randint

print('5')

for i in range(5):
    n = randint(100, 200)
    k = n//2 + 1
    print('{} {}'.format(n,k))
    if i%2==0:
        print('-1 '+ ('1 '*(n-2)) + '0')
    else:
        print('1 '+ ('-1 '*(n-2)) + '0')