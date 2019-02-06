
class Solution():

    def __init__(self):
        self.stack_a = []
        self.stack_b = []
    
    def push(self,data):
        self.stack_a.append(data)
    
    def pop(self):
        
        if self.stack_b == []:
            while self.stack_a:
                a = self.stack_a.pop()
                self.stack_b.append(a)
            return self.stack_b.pop()
            
        else:
            return self.stack_b.pop()
