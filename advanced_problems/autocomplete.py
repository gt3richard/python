
class Node:
    def __init__(self, value):
        self.children = {}
        self.word = False
        self.value = value

class Solution:
    def __init__(self, words):
        self.tree = None
        for word in words:
            for char in word:
                self.tree = self.__build(self.tree, char)

    def __build(self, node, char):
        if node is None:
            node = Node(char)
        else:
            if char not in node.children:
                node.children[char] = Node(char)
        node.word = True
        return node

s = Solution(['test', 'team'])
