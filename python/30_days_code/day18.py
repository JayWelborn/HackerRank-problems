class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self, char):
        self.stack.append(char)
        
    def enqueueCharacter(self, char):
        self.queue.append(char)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        char = self.queue.pop(0)
        return char