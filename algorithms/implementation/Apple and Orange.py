s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_left, apple_right = s - a, t - a
orange_left, orange_right = s - b, t - b

house_apples = len([x for x in apple if apple_left <= x <= apple_right])
house_oranges = len([x for x in orange if orange_left <= x <= orange_right])

print(house_apples)
print(house_oranges)

