# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = Node(0)
        carry = 0

        while (l1.val!= None or l2.val != None):
            sum=0
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum // 10
            if carry != 0:
                newNode = Node(0)
                dummy.next = newNode
            else:
                newNode = Node(sum)
                dummy.next = newNode
                carry = 0
            
            return dummy




