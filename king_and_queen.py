# https://www.youtube.com/watch?v=4HfDrisG3MQ
class Solution:
    def __init__(self, queen):
        self.queen = queen

    # If the x or y coordinates are the same or
    # the distance between the x and y coordinates of the king and queen are the same
    # then they are on an intersecting path on the board.
    def inDanger(self, king):
        print(self.queen[0] == king[0] or self.queen[1] == king[1] or abs(king[0] - self.queen[0]) == abs(king[1] - self.queen[1]))

s = Solution([1,2])

s.inDanger([1,4])