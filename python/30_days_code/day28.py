import re


N = int(input().strip())
names = []

for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    if re.match(r'[a-z]', firstName) and emailID.endswith('@gmail.com'):
        names.append(firstName)
        
[print(x) for x in sorted(names)]
