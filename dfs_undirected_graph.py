class Solution:
    def __init__(self, vertices, connections):
        self.vertices = vertices
        self.connections = connections
        self.visited = []

    def depthFirstSearch(self):
        for vertex in self.vertices:
            self.__visit(vertex)
    
    def __visit(self, vertex):

        # If you haven't visited the node before, print and mark it as visited so you don't duplicate
        # visiting the node and get stuck in a cycle.
        if not vertex in self.visited:
            self.visited.append(vertex)
            print(vertex)

            # Recursively check all the connecting nodes
            for connection in self.connections[vertex]:
                self.__visit(connection)

#
# A - B - C
#      \ /
#       D
#
#  E - F     G
#

s = Solution(['A', 'B', 'C', 'D', 'E', 'F', 'G'], {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E'],
    'G': []
})
s.depthFirstSearch()