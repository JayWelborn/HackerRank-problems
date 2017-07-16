arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
hourglass_sum = -1000000000
    
for i in range (4):
    for j in range (4):
        current = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if current >= hourglass_sum:
            hourglass_sum = current
            
print(hourglass_sum)
