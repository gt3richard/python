
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, bl, tr):
        self.bl = bl
        self.tr = tr

class Solution:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    # Looking at a plotting, you can take the innermost points using min / max to determine the 
    # coordinates of the inner overlapping rectangle.
    #
    # For example, just looking at the x axis, when comparing the rightmost x-coordinates, taking the MIN would yield the rightmost x-coordinate
    # of the inner overlapping rectangle. Then taking the MAX of the leftmost x-coordinates, would yield the leftmost x-coordinate. The
    # distance between these points is the x length of the overlapping rectangle. Repeat this same step for the y-coordinates.
    #
    def overlap(self):
        x = min(r1.tr.x, r2.tr.x) - max(r1.bl.x, r2.bl.x)
        y = min(r1.tr.y, r2.tr.y) - max(r1.bl.y, r2.bl.y)
        if x > 0 and y > 0:
            print(x * y)
        else:
            print(0)

#                 tr
#         |------F
#   |-----|--B   |
#   |     | *|   | 
#   |     E--|---|
#   A--------|
#   bl       
#
#   x = min (Bx, Fx) - max(Ax, Ex)
#   y = min (By, Fy) - max(Ay, Ey)
#   area = x * y
#

r1 = Rectangle(Point(2, 1), Point(5, 5))
r2 = Rectangle(Point(3, 2), Point(5, 7))
s = Solution(r1, r2)
s.overlap()

r1 = Rectangle(Point(2, 1), Point(5, 5))
r2 = Rectangle(Point(2, 2), Point(5, 7))
s = Solution(r1, r2)
s.overlap()