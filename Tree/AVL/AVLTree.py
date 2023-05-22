from AVLNode import AVLNode

class AVLTree:
    def __init__(self)-> None:
        self.root = None
        self.height = 1
    
    def insert(self, key):

        self.root = self.insertRec(self.root, key)

    def insertRec(self, node, key):

        #  Step 1-Perform normal BST
        if node is None:
            return AVLNode(key)
        
        if key < node.data:
            node.left = self.insertRec(node.left, key)

        elif key > node.data:
            node.right = self.insertRec(node.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        node.height = max(self.getHeight(node.left),
                          self.getHeight(node.right)) + 1

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - If the node is unbalanced,
        """
        ALWAYS Compare root node with root node left or right
        """
         # Case 1 - Left Left
        if balance > 1 and key < node.left.data:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and key > node.right.data:
            return self.left_rotate(node)
 
        # Case 3 - Left Right
        if balance > 1 and key > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
 
        # Case 4 - Right Left
        if balance < -1 and key < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def deletion(self, key):

        self.root = self.deletionRec(self.root, key)
    # Perform BST deletion
    def deletionRec(self, node, key):
            
        if node is None:
            return node
        
        if key < node.data:
            node.left = self.deletionRec(node.left, key)
        elif key > node.data:
            node.right = self.deletionRec(node.right, key)

        else:
            if node is None:
                return node

            elif node.left is None:
                temp= node.right
                node = None
                return temp
            
            elif node.right is None:
                temp= node.left
                node = None
                return temp

            temp = self.getMinValue(node.right)
            node.data = temp.data

            node.right = self.deletionRec(node.right,temp.data)

            node.height = max(self.getHeight(node.left),
                            self.getHeight(node.right)) + 1
        #  Balance factor
        balance = self.getBalance(node)

         # Case 1 - Left Left
        if balance > 1 and self.getBalance(node.left)>=0:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(node.right)<=0:
            return self.left_rotate(node)
 
        # Case 3 - Left Right
        if balance > 1 and  self.getBalance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        

        return node
                
        

    def left_rotate(self, node):
        x = node
        y = x.right

        x.right = y.left
        y.left = x

        x.height = 1 + max(self.getHeight(x.left),
                          self.getHeight(x.right)) 

        y.height = 1 + max(self.getHeight(y.left),
                                    self.getHeight(y.right)) 
        return y
    
    def right_rotate(self, node):
        x = node
        y = x.left

        x.left = y.right
        y.right = x

        x.height  = 1 + max(self.getHeight(x.left),
                               self.getHeight(x.right))

        y.height  = 1 + max(self.getHeight(y.left),
                                    self.getHeight(y.right))

        return y
  
    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def getHeight(self, node):
        if node is None:
             return -1
        return node.height
    
    def getMinValue(self, node):
        curr = node
        while (curr.left):
            curr = curr.left
        return curr
    
    def preOrder(self):
        
        def preOrderRec(node):
            if node is None:
                return
            print("{} ".format(node.data), end=" ")
            preOrderRec(node.left)
            preOrderRec(node.right)
        preOrderRec(self.root)

avl = AVLTree()
avl.insert(3)
avl.insert(1)
avl.insert(4)
avl.insert(10)
avl.insert(12)
avl.insert(8)
avl.insert(9)
avl.insert(2)
avl.preOrder()
print("**************")
avl.deletion(1)
avl.preOrder()