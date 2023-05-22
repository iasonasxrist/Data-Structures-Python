from AVLNode import AVLNode

class AVLTree:
    def __init__(self)-> None:
        self.root = None
        self.height = 1
    
    def insert(self,key):
        self.root = self.insertRec(self.root, key)

    def insertRec(self, node, key):

        if node is None:
            return AVLNode(key)
        
        if key < node.data:
           node.left = self.insertRec(node.left, key)
        else:
           node.right = self.insertRec(node.right, key)
        
        node.height = 1 + max(self.getHeight(node.left),
                           self.getHeight(node.right))


        balance = self.getBalance(node)


        # L-L
        if balance >1 and key < node.left.data:
            return self.rotate_right(node)
        # R-R
        if balance <-1 and key > node.right.data:
            return self.rotate_left(node)
        # L-R
        if balance >1 and key > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # R-L
        if balance <-1 and key > node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    

    def deletion(self,key):
        self.root = self.deletioRec(self.root, key)
    def deletioRec(self, node, key):
        if node is None:
            return node
        elif key < node.data:
            node.left = self.deletioRec(node.left, key)
        elif key > node.data:
            node.right = self.deletioRec(node.right, key)

        else:
            if node is None:
                return
            elif node.left is None:
                temp=node.right
                node=None
                return temp
            elif node.right is None:
                temp=node.left
                node=None
                return temp
            
            temp =  self.getMinValue(node.right)
            node.data = temp.data
           
            node.right = self.deleteRec(node.right, temp.data)

            node.height = max(self.getHeight(node.left),
                            self.getHeight(node.right)) + 1
        
        balance= self.getBalance(node)

        # L-L
        if balance >1 and self.getBalance(node)>=0:
            return self.rotate_right(node)
        # R-R
        if balance <-1 and self.getBalance(node)<=0 :
            return self.rotate_left(node)
        # L-R
        if balance >1 and self.getBalance(node)<0 :
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # R-L
        if balance <-1 and self.getBalance(node)>0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        

        return node

    def rotate_right(self,node):
        x = node
        y = x.left

        x.left= y.right
        y.right = x

        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))

        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    
    def rotate_left(self, node):
        x = node
        y = x.right

        x.right = y.left
        y.left = x

        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))
        
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        return y

    def getHeight(self, node):
        if node is None:
            return -1
        return node.height
    
    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def getMinValue(self, node):
        curr = node
        while (curr.left):
            curr = curr.left
        return curr
    def preOrder(self):

        def preOrderRec(node):
            if node is None:
                return
            print(node.data)
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
