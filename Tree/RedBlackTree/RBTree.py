from Node import Node

class RBTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):

        newNode = Node(key)
        if (self.root is None):
            self.root = newNode
        else:
            # recursive function
            self.insertNode(self.root, newNode)

            # check violation
            self.checker(newNode)
        self.size+=1
        self.root.isBlack=True

    def insertNode(self, node, newNode):
        if node is None:
                node = newNode
                return 
        
        if (newNode.data <= node.data):
            if node.left == None:
                    node.left = newNode
                    newNode.parent = node
                    newNode.isLeftChild = True
                    return
            self.insertNode(node.left, newNode)

        else:
            # (newNode.data > node.data)
            if node.right == None:
                    node.right = newNode
                    newNode.parent = node
                    newNode.isLeftChild = False
                    return 
            self.insertNode(node.right, newNode)
        

    def checker(self, node):
        if (node == self.root):
                node.isBlack==True
                return 
        # If two consecutive Red Nodes appeared 
        if (node.isBlack == False and node.parent.isBlack == False):
            self.correctTree(node)
        
        self.checker(node.parent)
    


    def correctTree(self, node):
        
        if (node.isLeftChild):
            # Rotation
            if (node.parent.parent.right is None or node.parent.parent.right.isBlack):
                return self.rotateTree(node)
            
            # Color-Flip
            else:
                if (node.parent.parent.right !=None):
                    node.parent.parent.right.isBlack = True
                node.parent.isBlack = True
                node.parent.parent.isBlack=False
        else:
            # Rotation
                if (node.parent.parent.left is None or node.parent.parent.left.isBlack ):
                    return self.rotateTree(node)
                
                # Color-Flip
                else:
                    if (node.parent.parent.left !=None):
                        node.parent.parent.left.isBlack = True
                    node.parent.isBlack = True
                    node.parent.parent.isBlack=False

    def rotateTree(self, node):
        if (node.isLeftChild):
            # if parent node 
            if (node.parent.isLeftChild):
                    self.right_rotate(node.parent.parent)
                    node.isBlack = False
                    node.parent.isBlack = True
                    node.parent.right.isBlack = False
                    
            else:
                    self.rightLeftRotation(node.parent.parent)
                    node.isBlack=True
                    node.right.isBlack = False
                    node.left.isBlack = False

        else:

            if (node.parent.isRightChild):
                self.left_rotate(node.parent.parent)
                node.isBlack = False
                node.parent.isBlack = True
                node.parent.left.isBlack = False

            else:
                self.leftRightRotation(node.parent.parent)
                node.isBlack = True
                node.right.isBlack = False
                node.left.isBlack = False

    
    def right_rotate(self, node):
        if node is None: return 
        x = node.left
        y = x.left
        x.left = y.right
        y.right = x
        

        if (node.parent is None ):
            self.root = x

        else:
                if (node.isLeftChild):
                    x.isLeftChild = True
                    x.parent.left = x
                else:
                    x.isLeftChild = False
                    x.parent.right = x

        if(x.right is not None):
            node.left=x.right
            node.left.isLeftChild=True
            node.left.parent=node
        else:
            node.left=None

        x.right=node
        node.parent=x
        node.isLeftChild=False

    def left_rotate(self, node):
        
        if node is None: return
        x = node.left
        y = x.right
        x.right = y.left 
        y.parent = x.parent

        if(node.parent==None):
            self.root = x
        else:

            if(node.isLeftChild):
                x.isLeftChild = True
                x.parent.left = x
            else:
                x.isLeftChild = False
                x.parent.right = x

        if(x.left is not None):
            node.right=x.left
            node.right.isLeftChild=False
            node.right.parent=node
        else:
            node.right=None

        x.left=node
        node.parent=x
        node.isLeftChild=True

    def leftRightRotation(self, node):
        self.leftRotation(node.left)
        self.rightRotation(node)

    def rightLeftRotation(self, node):
        self.rightRotation(node.right)
        self.leftRotation(node)

    def preOrder(self):
        self.preOrderRec(self.root)
    
    def preOrderRec(self, node):
        if node is None:
            return 
        print(node.data)
        self.preOrderRec(node.left)
        self.preOrderRec(node.right)

    def inOrder(self):
        self.inOrderRec(self.root)
    
    def inOrderRec(self, node):
        if node is None:
            return 
        print(node.data)
        self.inOrderRec(node.left)
        self.inOrderRec(node.right)

tree=RBTree()
tree.insert(7)
tree.insert(6)
tree.insert(5)
tree.insert(4)
tree.insert(3)
# tree.insert(2)
# tree.insert(1)

print("Inoder Traversal of Created Tree")
tree.inOrder()
print()
print("PostOrder Traversal of Created Tree")
tree.preOrder()