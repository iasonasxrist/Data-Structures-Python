from Node import Node
import sys
sys.setrecursionlimit(1000000)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):

        if (self.head == None):
            self.head = Node(element)
            return
        
        tmp = self.head
        while (tmp.next != None):
            tmp = tmp.next
        tmp.next = Node(element) # type: ignore
    
    def insertInSorted(self, element):

        if (self.head == None ):
            self.head = Node(element)
            return
        
        if (self.head.data >= element):
            newNode = Node(element)
            newNode.next = self.head # type: ignore
            self.head = newNode
            return
        
        # 1nd Way
        prev = self.head
        next = self.head

        while (next != None):
            if (element <= next.data):
                node = Node(element)
                prev.next = node # type: ignore
                node.next = next # type: ignore
                return
            
            prev = next
            next = next.next

        # 2nd Way

        # tmp = self.head
        # while ( tmp != None):
        #     if (element >= tmp.data):
        #         newTemp = tmp.next
        #         tmpAfterElement = Node(element)
        #         tmp.next = tmpAfterElement  # type: ignore
        #         tmpAfterElement.next = newTemp  
        #         return
        #     tmp = tmp.next

    def search(self, key):

        tmp = self.head
        while(tmp!=None):
            if tmp.data == key:
                return print("success")
            tmp = tmp.next
            
    def print(self):
        tmp = self.head
        while (tmp != None):
            print(tmp.data," ")
            tmp = tmp.next
            
    def delete(self, key):
        if (not self.head ):
            return 

        if (self.head.data == key): # type: ignore
            self.head = self.head.next # type: ignore
            return 

        prev = self.head
        next = self.head
        while (next != None):
            if (next.data == key):
                prev.next = next.next  
                next = next.next
            #move
            else:
                prev = next
                next = next.next

    
    def reverse(self):
        prev=None
        next = self.head
        curr= self.head
        while (next!=None):
            
            next = next.next
            curr.next =  prev #type:ignore
            prev = curr
            curr = next
        self.head = prev

    def GetNth(self, index):

        tmp = self.head
        count = 0
        while (tmp != None):

            if (tmp.data == index):
                print(" {} Nth Node into index:{} ".format(tmp.data, count))
            count += 1  
            tmp = tmp.next
        return 

    def IterSearch(self, value):
            
            if (self.head == None):
               return print("Doesn't exists!")

            if self.head.data == value:
                return print("success")
            self.head = self.head.next          
            return self.IterSearch(value)



linked = LinkedList()
linked.insert(1)
linked.insert(3)
linked.insert(4)
linked.insert(5)
linked.insert(8)
linked.insert(9)
linked.insert(10)
linked.insert(14)
linked.print()
linked.insertInSorted(7)
print("******************")
# linked.search(3)

# linked.delete(5)
print("******************")
linked.insertInSorted(12)
linked.print()
linked.reverse()
print("******REVERSE************")
linked.print()
print("********NthNode********")
linked.GetNth(5)
linked.IterSearch(90)
# linked.print()