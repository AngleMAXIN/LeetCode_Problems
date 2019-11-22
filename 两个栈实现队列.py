class Solution:
    input_stack = []
    output_stack = []
    
    def push(self, node):
        self.input_stack.append(node)
        print("len:",self.input_stack)
    def pop(self):
        # return xx
        if not self.output_stack:
            while self.input_stack:
                popItem = self.input_stack.pop(-1)
                self.output_stack.append(popItem)
        return self.output_stack.pop(-1)

s = Solution()
s.push(1)
s.push(2)
s.push(3)
res = s.pop()
print(res)
res = s.pop()
print(res)
s.push(4)
print(s.pop())
print(s.pop())