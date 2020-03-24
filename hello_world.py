
input = 'Hello World'

class Solution:
    def __init__(self, msg):
        print('Setup')
        self.msg = msg

    def message(self):
        return self.msg

s = Solution('Hello World')
output = s.message()

assert input == output, 'Not Equal'