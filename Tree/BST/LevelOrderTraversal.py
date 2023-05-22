from collections import deque
class Node:
    # A utility function to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Iterative Method to print the
# height of a binary tree
 
 
def printLevelOrder(root):
    # Base Case
    res=[]
    # if root is None:
    #     return
 
    # Create an empty queue
    # for level order traversal
    queue = deque()
 
    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue))>0:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            res.append(level)

    return res


 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level Order Traversal of binary tree is -")
print(printLevelOrder(root))

# 590. N-ary Tree Postorder Traversal
def postorder(self, root: 'Node') -> List[int]:
    res = []

    def postorderRec(root):
        if root is None:
            return 
        for child in root.children:
            postorderRec(child)
            res.append(child.val)
        
    if root is None:
        return None
    postorderRec(root)
    res.append(root.val)
    
    return res

