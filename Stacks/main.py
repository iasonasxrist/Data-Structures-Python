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

stack = Stack()

print("Stack based on Array\n")
stack.testCases()


