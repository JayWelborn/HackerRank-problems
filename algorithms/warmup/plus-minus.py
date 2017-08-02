n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = []
negative = []
zeros = []

for i in range(len(arr)):
    if arr[i] > 0:
        positive.append(arr[i])
    elif arr[i] < 0:
        negative.append(arr[i])
    else:
        zeros.append(arr[i])
        
print(len(positive)/len(arr))
print(len(negative)/len(arr))
print(len(zeros)/len(arr))