from Node import Node

class BTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        self.root = self.insertRec(self.root, data)

    def insertRec(self, node, data):
        
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insertRec(node.left, data)
        else:
            node.right = self.insertRec(node.right, data)
        return node
    

    def preorder(self):
        def preorderRec(node):
        
            if node is None:
                return
            print(node.data, end=' ')
            preorderRec(node.left)
            preorderRec(node.right)
  
        preorderRec(self.root)
    
    def inorder(self):
        def inorderRec(node):
            if node is None:
                return
            inorderRec(node.left)
            print(node.data, end=' ')
            inorderRec(node.right)
            

        inorderRec(self.root)


    def postorder(self):
        def postorderRec(node):
            if node is None:
                return
            postorderRec(node.left)
            postorderRec(node.right)
            print(node.data, end=' ')

        postorderRec(self.root)

    def search(self,key):

        def searchInto(node, key):
            if node is None:
                return  print("Error")
            
            if node.data == key:
                return print("success \n")
            
            if key < node.data:
                
                return searchInto(node.left, key)
            else:
               return  searchInto(node.right, key)
        
        return searchInto(self.root, key)
            
    def maxDepthLen(self):
        def maxDepthRec(node):
            
            if node is None:
                return 0
            print(node.data)
        
            return max(maxDepthRec(node.left), maxDepthRec(node.right)) +1
        return maxDepthRec(self.root)
    
    def maxSumFromRootToAnyLeaf(self):
        def maxSumRec(node):
            if node is None:
                return 0
            return max(maxSumRec(node.left), maxSumRec(node.right)) + node.data
            
        return maxSumRec(self.root)
        
    def minValueNode(self, node):
            current = node
            
            while (current.left):
                print("cur", current)
                current = current.left

            return current
    
    def deletion(self, key):

        self.root =  self.deletionRec(self.root, key)

    def deletionRec(self, node, key):
            
            if node is None:
                return 
            
            if (key < node.data):
                node.left = self.deletionRec(node.left, key)

            elif (key > node.data):
                node.right = self.deletionRec(node.right, key)

            # Case key == node.data
            else:
                # Case  One Child 
                if not node.left and not node.right:
                    return None
                
                elif node.left is None:
                    temp = node.right
                    print("....",temp)
                    node = None
                    return temp

                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                
                # Case Two Childs
                else:
               
                    print("node.right",node.right.data)
                    temp = self.minValueNode(node.right)
                
                    # Delete and replace by depthest value
                    node.data = temp.data

                    node.right = self.deletionRec(node.right, temp.data)
            return node


    def isBalanced(self) -> bool:
        self.root = self.isBalancedRec(self.root,1)

    def isBalancedRec(self, node, h):
            if node is None: 
                return h
            left = self.isBalancedRec(node.left, h+1)
            if not left : return 
            right = self.isBalancedRec(node.right, h+1)
            if not right : return
            
            return abs(left-right)<=1 and max(left,right)


btree = BTree()

btree.insert(15)
btree.insert(3)
btree.insert(20)
btree.insert(10)
btree.insert(18)
btree.insert(30)
btree.insert(25)
btree.preorder()
print("\n")
btree.inorder()
print("\n")
btree.postorder()
btree.search(15)
print("count",btree.maxDepthLen())
print(btree.maxSumFromRootToAnyLeaf())
# btree.insert(9)
btree.preorder()
btree.deletion(20)
print("deleted tree")
btree.preorder()
print(btree.isBalanced())
