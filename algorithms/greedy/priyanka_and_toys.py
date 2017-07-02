# number of toys
num_toys = int(input().strip())

# weight array
toy_weights = sorted([int(x) for x in input().strip().split(' ')])

# array of toys paid for
toys_bought = []

weight_placeholder = 0

for i in range(len(toy_weights)):
    
    toy = toy_weights.pop(0)
    
    if len(toys_bought) >0 and toy <= weight_placeholder + 4:
        pass
    else:
        toys_bought.append(i)
        weight_placeholder = toy
        
print(len(toys_bought))
    
