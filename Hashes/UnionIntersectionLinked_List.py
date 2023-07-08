class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert(self, element):
        if not self.head:
            self.head = Node(element)
            return

        tmp = self.head
        while (tmp.next != None):
            tmp = tmp.next
        tmp.next = Node(element)

    def search(self, element):
        tmp = self.head
        while (tmp != None):
            if tmp.data == element:
                return True
            tmp = tmp.next
        return False

def Intersection(head1, head2):
    # create a set
    hashmap = set()
    # create a LinkedList
    intesection = LL()

    while (head1 != None):
        data = head1.data
        hashmap.add(data)
        head1 = head1.next

    while (head2 != None):
        data = head2.data
        if data in hashmap:
            intesection.insert(data)
        head2 = head2.next

    return intesection.head


def Union(head1, head2):
    ans = LL()
    while (head1 != None):
        data = head1.data
        ans.insert(data)
        head1 = head1.next

    while (head2 != None):
        data = head2.data
        if ans.search(data) == False:
            ans.insert(data)
        head2 = head2.next

    return ans.head

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == '__main__':

    # first list
    ll1 = LL()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)
    ll1.insert(5)

    # second list
    ll2 = LL()
    ll2.insert(5)
    ll2.insert(6)
    ll2.insert(7)
    ll2.insert(8)

    print("First list is ")
    printList(ll1.head)

    print("Second list is ")
    printList(ll2.head)

    print("Intersection list is")
    printList(Intersection(ll1.head, ll2.head))

    print("Union list is")
    printList(Union(ll1.head, ll2.head))
