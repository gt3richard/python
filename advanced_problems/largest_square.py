#https://youtu.be/FO7VXDfS8Gk

class Solution:
    def __init__(self, matrix):
        self.max = 0
        self.matrix = matrix

    def findLargestSquare(self):
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[0])):

                # Make sure you're not evaluating the edges where the largest would always be 1 since it can't extend beyond the boundaries of the matrix.
                if x != 0 and y != 0:
                    
                    # Boolean logic that if you're current node is 1 none of the 3 surrounding nodes are 0 then you have a square of 1's.
                    # Update the current node value to 2 since it's a 2x2 matrix. As you iterate you'll come across a case where 
                    # all surround squares are 2 which means it's surrounded by 2x2 matricies so this is a 3x3.
                    self.matrix[x][y] += min(self.matrix[x-1][y-1], self.matrix[x][y-1], self.matrix[x-1][y])

                # Keep track of the max
                self.max = max(self.matrix[x][y], self.max)
        print(self.max)

#(x-1, y-1) (x, y-1)
#(x-1, y)   (x, y)

#101
#111
#111
matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
s = Solution(matrix)
s.findLargestSquare()


#10110
#01110
#01111
#11110
#11111
matrix = [[1,0,1,1,0], [0,1,1,1,0], [0,1,1,1,1], [1,1,1,1,0],[1,1,1,1,1]]
s = Solution(matrix)
s.findLargestSquare()