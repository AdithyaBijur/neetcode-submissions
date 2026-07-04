"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def getNode(i,j, size):
            s = 0
            for ii in range(i,i + size):
                for jj in range(j, j + size):
                    s += grid[ii][jj]
            if s== 0 or s == size * size:
                return Node(s != 0, True,None, None, None, None)
            return Node(False, False, getNode(i,j, size//2),getNode(i, j+ size//2, size//2),getNode(i + size//2, j, size//2),getNode(i+size//2, j+ size//2, size//2))


        return getNode(0,0, len(grid))    