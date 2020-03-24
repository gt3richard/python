class Solution:
    def __init__(self, array):
        self.array = array

    # Assuptions are you only traverse forward, don't loop, and start at index 0
    def findCycle(self):
        a = 0
        b = 0

        while True:

            # If your indexes are out of bounds (negative or larger than array) then you've traversed as far as possible
            if (self.array[a] < 0 or self.array[b] < 0 and self.array[a] >= len(self.array) or self.array[b] >= len(self.array)):
                return False

            # Move 'a' once
            a = self.array[a]

            # Test if a is now outside
            if(self.array[a] < 0 or self.array[a] >= len(self.array)):
                return False

            # If you move one pointer faster than the other then at some point if there is a cycle they would run into each other.
            # This verifies that condition
            if (a == b):
                return True

            # Move 'a' a second time
            a = self.array[a]
            if(self.array[a] < 0 or self.array[a] >= len(self.array)):
                return False

            if (a == b):
                return True

            # Move 'b' only once
            b = self.array[b]
            
            if(self.array[b] < 0 or self.array[b] >= len(self.array)):
                return False

            if (a == b):
                return True


s = Solution([1,2,3,4,5])
print(s.findCycle())

s = Solution([1,2,3,1,5])
print(s.findCycle())

s = Solution([1,3,4,6,7,8,7])
print(s.findCycle())