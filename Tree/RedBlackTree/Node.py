
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.isBlack = False
        self.isLeftChild = False

"""
Rules
        Root is always Black |  New insertiosn are always Red |
        Nulls are Black |
        Every path has the same number of Black Nodes | 
        No two consecutive Red Nodes |
Rebalancing
   
    BLACK AUNT ROTATE:
             BLACK : PARENT | RED : CHILDREN

    RED AUNT COLOR-FLIP

    BLACK : PARENT | RED : CHILDREN
"""