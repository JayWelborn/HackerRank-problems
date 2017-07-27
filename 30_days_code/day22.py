 def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1