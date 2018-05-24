group_size = int(input())
rooms = [int(x) for x in input().split()]
all_rooms = set()
repeat_rooms = set()

for room in rooms:
    if room in all_rooms:
        repeat_rooms.add(room)
    else:
        all_rooms.add(room)
        
print(all_rooms.difference(repeat_rooms).pop())
