
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            tleft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tright = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bleft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bright = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

            if tleft.isLeaf and tright.isLeaf and bleft.isLeaf and bright.isLeaf and \
                tleft.val ==  tright.val ==  bleft.val ==  bright.val:
                return Node(tleft.val, True, None, None, None, None)
            else:
                return Node(False, False, tleft, tright, bleft, bright)
