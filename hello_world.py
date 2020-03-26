class Solution:
    def __init__(self, msg):
        print('Setup')
        self.msg = msg

    def message(self):
        return self.msg

s = Solution('Hello World')
output = s.message()


assert 'Hello World' == output, 'Not Equal'