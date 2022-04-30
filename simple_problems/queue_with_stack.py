class Solution:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    # Recursively take each value off the stack save hold until you've printed the 
    # result you want. Then add the remaining values back to the stack
    def pop(self):
        if len(self.stack) == 0:
            print('None')
        elif len(self.stack) == 1:
            print(self.stack.pop())
        else:
            val = self.stack.pop()
            self.pop()
            self.stack.append(val)

s = Solution()

s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.push(4)
s.pop()
s.pop()
s.pop()