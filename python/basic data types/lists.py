if __name__ == '__main__':
    N = int(input())
    l = []
    
    for i in range(N):
        # get command line arguments and store them as a list
        command = input().split(' ')
        
        if command[0] == 'print':
            print(l) 
            
        elif len(command) == 1:
            eval('l.{}()'.format(command[0]))
        
        elif len(command) == 2:
            eval('l.{0}({1})'.format(command[0], command[1]))
            
        elif len(command) == 3:
            eval('l.{0}({1},{2})'.format(command[0], command[1], command[2]))
            
        
