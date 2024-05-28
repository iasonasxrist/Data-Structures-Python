# Implementation using Array

class Stack:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.count = 0
        self.stack = []

    def pop(self):
        
        if not self.isEmpty():
            
            self.count -= 1
            return self.stack.pop()
         
        else:
            print("Stack is ready for insertions!")
            return

    def push(self, value):
        if self.isFull():
            print("Stack out of capacity")
            return 
        self.count += 1
        self.stack.append(value)
        

    def peek(self):
        if not self.isEmpty():
            topElement = self.stack[-1]
            print(f"Top element of the stack is {topElement}.")
            return
        
        print("Stack is empty. No element to peek!")
        return None

    def isFull(self) :
        return self.count == self.max_capacity
    
    def isEmpty(self):
        return len(self.stack) == 0

    def testCases():

        stack  =  Stack(5)

        # Edge cases for empty stack
        stack.pop()
        stack.peek()

        # Normal working cases
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(2)

        stack.pop()
        stack.pop()
        stack.push(2)
        stack.push(2)

        # After operations
        stack.peek()

        if stack.isEmpty():
            print("Stack is Empty")
        else :
            print("Keep adding values\n")


        print(stack.stack , stack.max_capacity)

# stack = Stack()

print("Stack based on Array\n")
# stack.testCases()



# Implementation using LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:

    def __init__(self):
        self.head = None


    def push(self, value):

        if self.head == None:
            newNode = Node(value)
            self.head = newNode
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode


    def pop(self):

        if not self.isEmpty():
            poppedNode = self.head
            self.head = self.head.next 
            poppedNode.next = None
            return poppedNode.data
        else:
            print("Stack is empty!")
            return 
         
    def peek(self):

        if self.isEmpty():
            return None
        
        else:
            return self.head.data

    def isEmpty(self):
      if self.head == None:
          return True
      else :
          return False

    def peek(self):
        pass

    def display(self):

        iterNode = self.head
        if self.isEmpty():
            print("Stack Underflow")

        else:

            while (iterNode != None):
                print("",iterNode.data)
                iterNode = iterNode.next 
                if (iterNode != None):
                    print(" -> ", end = "")

            return

    def testCases(self):
            print("Running test cases...\n")
            
            # Test case 1: Push elements onto the stack
            print("Test Case 1: Push elements onto the stack")
            self.push(11)
            self.push(22)
            self.push(33)
            self.display()
            
            # Test case 2: Pop an element from the stack
            print("\nTest Case 2: Pop an element from the stack")
            self.pop()
            self.display()
            
            # Test case 3: Peek at the top element of the stack
            print("\nTest Case 3: Peek at the top element of the stack")
            top_element = self.peek()
            print("Top element of the stack:", top_element)
            
            # Test case 4: Push more elements to fill the stack to capacity
            print("\nTest Case 4: Push more elements to fill the stack to capacity")
            self.push(44)
            self.push(55)
            self.push(66)
            self.push(77)
            self.display()
            
            # Test case 5: Try pushing more elements when the stack is full
            print("\nTest Case 5: Try pushing more elements when the stack is full")
            self.push(88)
            
            # Test case 6: Pop all elements from the stack
            print("\nTest Case 6: Pop all elements from the stack")
            while not self.isEmpty():
                self.pop()
                self.display()
            
            # Test case 7: Peek when the stack is empty
            print("\nTest Case 7: Peek when the stack is empty")
            self.peek()
            
            print("\nAll test cases executed.")

stack = StackLinkedList()

print("Stack based on LinkedList\n")
stack.testCases()



import math
# Delete Middle element
st = ['1', '2', '3', '4', '5', '6', '7']
v = []

while st:
    v.append(st.pop(0))

n = len(v)
print(v)  # Output: ['7', '6', '5', '4', '3', '2', '1']


if n % 2 == 0 :
    target = math.floor(n/2)
    for i in range(0,n):
        if target == i:
            continue
        st.append(v[i])
else:
     target = math.floor(n/2)
     for i in range(0,n):
        if target == i:
            continue
        st.append(v[i])

while len(st)> 0 :
    p = st[0]
    del st[0]
    print(p, end = "")


st = Stack(10)
st.push('1')
st.push('2')
st.push('3')
st.push('4')
st.push('5')
st.push('6')
st.push('7')

def deleteMid(stack, n , curr):
    if stack.isEmpty() or stack.isFull():
        return 
    
    x = stack.peek()
    st.pop()

    deleteMid(stack, n, curr +1)
    
    if (curr != int(n/2)):
        st.push(x)

deleteMid(st, st.max_capacity, 0)

while not stack.isEmpty():
    p = stack.peek()
    st.pop()
    print(str(p) + " ", end="")

        
    
