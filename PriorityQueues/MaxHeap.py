class MaxHeap:

    def __init__(self, maxHeapSize):
        self.heapSize = maxHeapSize
        self.size = 0
        self.heap = [0] * self.heapSize

    def parent(self, pos):
        return (pos-1)//2

    def leftChild(self, pos):
        return (2 * pos)+1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def insert(self, key):
        if (self.size == self.heapSize):
            print("\nOverflow: Could not insertKey\n")
            return None

        self.heap[self.size] = key

        curr_pos = self.size

        while (curr_pos != 0 and self.heap[curr_pos] > self.heap[self.parent(curr_pos)]):

            self.swap(curr_pos, self.parent(curr_pos))
            curr_pos = self.parent(curr_pos)
        self.size += 1

    def swap(self, curr_pos, parent):
        tmp = self.heap[curr_pos]
        self.heap[parent], self.heap[curr_pos] = tmp, self.heap[parent]

    def maxHeapify(self, pos):
        left = self.leftChild(pos)
        right = self.rightChild(pos)
        largest = pos

        if (left < self.size and self.heap[left] > self.heap[pos]):
            largest = left

        if (right < self.size and self.heap[right] > self.heap[largest]):
            largest = right

        if (largest != pos):

            temp = self.heap[pos]
            self.heap[pos] = self.heap[largest]
            self.heap[largest] = temp
            self.maxHeapify(largest)

    def extractMax(self):
        if self.size <= 0:
            return None

        # Store Max
        if self.size == 1:
            self.heapSize -= 1
            return self.heap[0]

        max = self.getMax()

        # Make last element, Root
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap = self.heap[:-1]

        # Restore the Max Heap
        self.maxHeapify(0)
        return max

    def getMax(self):
        if self.size == 0:
            return None

        return self.heap[0]

    def getMin(self):
        minl = -1
        count = 0
        while (count < self.size):
            minl = max(minl, self.heap[count])
            count += 1

        return minl

    def isLeaf(self, pos):
        if (pos > self.size//2 or pos > self.size):
            return True
        return False

    # def printHeap(self):
    #     count = 0
    #     print(self.heapSize)
    #     while (count < self.size):
    #         print("Value {} has parent {}, has left child {}, has right child{} "
    #               .format(self.heap[count], self.heap[self.parent(
    #                   count)], self.heap[self.leftChild(count)],  self.heap[self.rightChild(count)]))
    #         count += 1


if __name__ == '__main__':
    maxHeap = MaxHeap(10)
    maxHeap.insert(4)
    maxHeap.insert(6)
    maxHeap.insert(8)
    maxHeap.insert(10)
    maxHeap.insert(11)
    maxHeap.insert(15)
    maxHeap.insert(16)
    maxHeap.insert(18)
    maxHeap.insert(20)
    maxHeap.insert(84)

    print(maxHeap.getMax(), maxHeap.heap)
    # maxHeap.extractMax()

    count = 0
    while (count < maxHeap.size):
        print("Value is:", maxHeap.heap[count])
        count += 1
    # maxHeap.printHeap()
    print(maxHeap.heap)
