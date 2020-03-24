class Solution():
    def __init__(self, array1, array2, array3):
        self.array1 = array1
        self.array2 = array2
        self.array3 = array3

    def findOverlap(self):
        x = 0
        y = 0
        z = 0
        overlap = []

        while(x < len(self.array1) and y < len(self.array2) and z < len(self.array3)):
            # x = y = z
            if(self.array1[x] == self.array2[y] and self.array2[y] == self.array3[z]):
                overlap.append(self.array1[x])
                x += 1
                y += 1
                z += 1

            # x < y
            elif (self.array1[x] < self.array2[y]):
                x +=1

            # y < z (previous statement failed so x > y)
            elif (self.array2[y] < self.array3[z]):
                y += 1

            # z < x & y (both previous statements failed so x > y and y > z)
            else:
                z += 1
            
        print(overlap)


s = Solution([1,3,5,6,7,8], [3,4,7,9,10,11], [1,3,5,7,8,9])
s.findOverlap()