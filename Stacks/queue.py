# Implementation using Array

class Queue:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.count = 0
        self.queue = []

    def dequeue(self):
        
        if not self.isEmpty():
            
            self.count -= 1
            return self.queue.pop(0)
         
        else:
            print("Queue is ready for insertions!")
            return

    def enqueue(self, value):
        if self.isFull():
            print("Queue out of capacity")
            return 
        self.count += 1
        self.queue.append(value)
        

    def peek(self):
        if not self.isEmpty():
            topElement = self.queue[0]
            print(f"First element of the Queue is {topElement}.")
            return
        
        print("Queue is empty. No element to peek!")
        return None

    def isFull(self) :
        return self.count == self.max_capacity
    
    def isEmpty(self):
        return len(self.queue) == 0

    def testCases(self):


        # Edge cases for empty queue
        queue.dequeue()
        queue.peek()

        # Normal working cases
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(2)

        queue.dequeue()
        queue.dequeue()
        queue.enqueue(2)
        queue.enqueue(2)

        # After operations
        print("Peek at the front of the queue:", queue.peek())

        if queue.isEmpty():
            print("Queue is Empty")
        else:
            print("Keep adding values\n")

        print("Queue contents:", queue.queue)
        print("Max capacity:", queue.max_capacity)


# Create a Queue instance and run test cases
queue = Queue(5)
print("Queue based on Array\n")
queue.testCases()
