def is_prime(x):
    
    if x <=1:
        return False
    
    elif x <= 3:
        return True
    
    elif x%2==0 or x%3==0:
        return False
    
    for i in range(5, round(x**(1/2)) + 1):
        if x%i==0:
            return False
    
    return True

cases = int(input())
for _ in range(cases):
    case = int(input())
    if is_prime(case):
        print("Prime")
    else:
        print("Not prime")