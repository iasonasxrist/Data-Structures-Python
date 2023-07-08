from Node import Node
class Solution:
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
    
    def print(self):
        tmp = self.head
        while (tmp!= None):
            print(tmp.data, end=" ")
            tmp = tmp.next

    # crop-rotation example from geekforgeeks   
    def rotateRight(self, k):
        
        count = 0
        next = self.head
        knth = None
        while (k < count):
            next = next.next #type:ignore
            count +=1
        
        knth = next
        while (next.next != None): #type:ignore

            next = next.next #type:ignore
        
        next.next = self.head #type:ignore
        self.head = knth.next #type:ignore
        knth.next = None #type:ignore

    # 19. Remove Nth Node From End of List
    def RemoveNth(self,k):
        
        prev = self.head
        curr = self.head
        count = 0

        if self.head == None or self.head.next ==0 or k==0:
            return

   
        for _ in range(k):
            curr = curr.next #type:ignore
        
        if curr == None:
            return self.head.next
    
        while curr.next:
            prev = prev.next        #type: ignore
            curr = curr.next        #type: ignore
        prev.next = prev.next.next  #type: ignore
        return

    # 206. Reverse Linked List
    def reverse(self):
        curr = self.head
        prev = None
        while (curr !=None): 
            next = curr.next    
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    # 234. Palindrome Linked List
    def pallindrome(self):

        fast = self.head
        slow = self.head
        count = 0

        while (slow):
            slow  = slow.next
            count+=1
         
        elements=[]
        for _ in range(count//2):
            elements.append(fast.data)
            fast = fast.next

        if count % 2 !=0:
            fast = fast.next
        
        while (fast):
            if (not elements or fast.data != elements.pop()):
                return print("false")
            fast = fast.next

        return print("true")

    # 203. Remove Linked List Elements
    def removeElements(self, val):

        if self.head == None or self.head.next==None:
            return None
        dummy = Node()
        dummy.next = self.head
        curr = self.head
        while (curr.next!=None):
            if (curr.next.data == val):
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

    # 141. Linked List Cycle
    def hasCycle(self):

        if self.head == None or self.head.next==None:
            return False
        count = 0
        s = list()
        temp = self.head
        while(temp):
            count +=1
            if (temp in s):
                # return print(count)
                return True
            
            s.append(temp)
            temp = temp.next

        return False

#TODO
    # 92. Reverse Linked List II
    def reverseLinkedList(self, left, right):

        if self.head == None or self.head.next == 0 or left==right:
            return self.head
        curr = self.head
        temp = self.head
        
        #Set left value 
        for _ in range(left - 1):               
            curr = curr.next #type:ignore
            
        
        temp_curr = curr.next #type:ignore
         # Set as left.next ==2 
        print("Curr on left",temp_curr.data) #type:ignore
        for _ in range(right - left):    
            print("***********")
            nxt = temp_curr.next #type:ignore
            print("1oo", nxt.data)


            temp_curr.next = nxt.next  #type:ignore
            print("2o",nxt.next.data)


            nxt.next = curr.next #type:ignore
            print("3o",nxt.next.data) #type:ignore

            curr.next = nxt #type:ignore
            print("nxt4o",nxt.data) 
        return temp.next
        
    

    # 61. Rotate List
    def rotateList(self,k):
        # doesnt work properly in here

        if self.head ==0: return self.head

        count = 0
        zero = Node(0)
        zero.next = self.head
        curr = zero
        
        
        while (curr.next):
            count= count +1
            curr = curr.next
        
        k = k % count
        if not k: return self.head
        
        nxt = zero
        for _ in range(0,count-k):
            nxt = nxt.next
            # print(next.next.data)

        zero.next  = nxt.next 
        curr.next = self.head
        nxt.next = None

        return zero.next
    
linked = Solution()
linked.insert(20)
linked.insert(4)
linked.insert(15)
linked.insert(10)
linked.insert(5)
# hascycle experiment
# linked.head.next.next.next = linked.head.next
# print("linked",linked.head.next.next.next.data)
# print(linked.head.next.data)

# if linked.hasCycle():
#     print("Found")
# else:
#     print("Error")


# linked.rotateRight(2)
linked.rotateList(2)

linked.print()
# linked.RemoveNth(1)
# linked.reverse()
# linked.reverseLinkedList(1,3)


# palin = Solution()
# palin.insert(2)
# palin.insert(2)
# palin.insert(2)
# palin.insert(2)
# palin.pallindrome()
# palin.removeElements(2)
# palin.print()