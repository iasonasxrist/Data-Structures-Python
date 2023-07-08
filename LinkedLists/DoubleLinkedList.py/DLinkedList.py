from Node import Node

class DLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, element):

        #Create new Node
        new_node = Node(element)

        if (self.head == None):
            self.head = new_node
            return 
        
        tmp = self.head
        while (tmp.next != None):
            #Trasversing till last Node
            tmp = tmp.next

        # Set new Node
        tmp.next = new_node #type: ignore
        new_node.prev = tmp #type: ignore

        # set tail
        self.tail = new_node
    
    def insertSorted(self, element):
        #Create Head into empty DLL
        if (self.head == None):
            self.head = Node(element)
            self.head.prev = None
            return
        
        if (self.head.data >= element):
            #Create new Node
            newNode = Node(element)

            #Define new Node's values
            newNode.next = self.head #type: ignore
            newNode.prev = None

            if self.head is not None:
                 self.head.prev = newNode  #type: ignore

            #Set new Node as Head
            self.head =  newNode 
        
            return  

        back = self.head
        curr = self.head
        while (curr != None):
            print(curr.data)

            if (curr.data >= element):
                #Create new Node
                newNode = Node(element)

                back.next = newNode     #type: ignore
                newNode.next = curr    # type: ignore
                curr.prev = newNode     #type: ignore
                newNode.prev = back    #type: ignore    
                return 

            back = curr
            curr = curr.next
        
    def delete(self, key):
        if (not self.head):
            return 

        if (self.head.data == key): # type: ignore
            self.head = self.head.next # type: ignore
            self.head.prev = None  # type: ignore
            return 

        back = self.head
        next = self.head
        while (next != None):
            if (next.data == key):
                #Bypass back to next.next
                back.next = next.next
                next.next.prev = back  # type: ignore
                next = next.next
            #move
            else:
                back = next
                next = next.next

    def print(self):
        tmp = self.head
        ok = self.tail
        print("tail is:", ok.data) #type:ignore
        print("\nTranversal in forward direction")
        while (tmp != None):
            print("{}".format(repr(tmp.data)), end=" ")
            # print("{}".format(repr(tmp.prev)), end=" ")
            

            last = tmp

            tmp = tmp.next

        print("\nTranversal in reverse direction")
        while last: #type: ignore
            print("{}".format(repr(last.data)), end=" ")
            # print("{}".format(repr(last.prev)), end=" ")
           

            last = last.prev
        print("\n") 

    def printReverse(self):
        tmp = self.head
        while (tmp != None):
            
            print(tmp.data)
            tmp = tmp.next

    def search(self, key):

        tmp = self.head
        while(tmp!=None):
            if tmp.data == key:
                return print("success")
            tmp = tmp.next

    def reverse(self):

        back = None
        prev = None
        curr= self.head
        next = self.head
        while (curr!= None):
            back = curr
            next = curr.next    
            prev = curr.prev
            curr.next = prev
            curr.prev = next
            curr = next 

        self.head = back

                    
link = DLinkList()
link.insert(2)
link.insert(3)
link.insert(4)
link.insert(5)
link.insert(6)
link.insertSorted(5)
# print(" To 6 ***************")
# link.insert(7)
# link.insert(9)
# # del 2
# link.delete(2)
# link.print()
# print("\n To 9 ***************")
# # del 5
# link.delete(5)
# link.print()
print("\n***************")
# # del 3
link.delete(3)
link.print()
link.reverse()
print("\n***************")
link.printReverse()



