# Binary nodes can only have 2 children so assign left & right.
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
class Solution:
    def __init__(self, values):
        self.tree = None
        for value in values:
            self.tree = self.__build(self.tree, value)
            

    def __build(self, node, value):

        # If you're at the root or given a child that doesn't exist yet, then create it.
        if node is None:
            node = Node(value)
        else:

            # If the value is less than the current node then you're going down the left side of
            # the tree which should always be less than the right
            if value < node.value:

                # If you've reached the leaf then create a new node else keep recursively
                # iterating down the tree
                if node.left is not None:
                    self.__build(node.left, value)
                else:
                    node.left = Node(value)

            else:
                # Same logic as the left but just for the right side of the tree.
                if node.right is not None:
                    self.__build(node.right, value)
                else:
                    node.right = Node(value)

        return node


    def findMax(self):
        print(self.__max(self.tree))

    def __max(self, node):
        # In a balanced binary tree you can always assume the right most path would yield the max. 
        if node.right is None:
            return node.value
        else:
            return self.__max(node.right)


        
s = Solution([4,5,2,7,9,1])
# 9
s.findMax()

s = Solution([9,5,2,10,7,4,3,40,34,2,7,8,11,7,9,1])
# 40
s.findMax()

s = Solution([5])
# 5
s.findMax()