class MinHeap:

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

    def insert(self, new):
        if (self.size == self.heapSize):
            return None
        self.heap[self.size] = new
        curr_pos = self.size
        while (self.heap[curr_pos] < self.heap[self.parent(curr_pos)]):
            self.swap(curr_pos, self.parent(curr_pos))

        self.size += 1

    def swap(self, current, parent):
        tmp = self.heap[current]
        self.heap[parent], self.heap[current] = tmp, self.heap[parent]
        # return

    def extractMin(self):
        if (self.size == 0):
            return None
        # Store Min
        min = self.getMin()
        # Make last element, Root
        self.heap[0] = self.heap[self.size-1]
        # Remove Last Element
        self.heap = self.heap[:-1]
        self.size -= 1
        self.minHeapify(0)
        return min

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftChild(pos)] or self.heap[pos] > self.heap[self.rightChild(pos)]):
                if (self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]):
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
                else:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

    def getMin(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def getMax(self):
        if self.size == 0:
            return None
        maxl = -1
        count = 0
        while (count < self.size):
            maxl = max(self.heap[count], maxl)
            count += 1
        return maxl

    def isLeaf(self, pos):
        if (pos >= self.size//2) and (pos < self.size):
            return True
        return False

# It's for informational purpose May bug occurs
    def printHeap(self):
        count = 0
        print(self.heapSize)
        while (count <= self.heapSize):
            print("Value {} has parent {}, has left child {}, has right child{} "
                  .format(self.heap[count], self.heap[self.parent(
                      count)], self.heap[self.leftChild(count)],  self.heap[self.rightChild(count)]
                      if not (self.heap[self.rightChild(count)] == IndexError) else None))
            count += 1


if __name__ == '__main__':
    minHeap = MinHeap(10)
    minHeap.insert(4)
    minHeap.insert(6)
    minHeap.insert(8)
    minHeap.insert(10)
    minHeap.insert(11)
    minHeap.insert(15)
    minHeap.insert(16)
    minHeap.insert(18)
    minHeap.insert(20)
    minHeap.insert(84)

    # print(minHeap.getMax())
    minHeap.extractMin()

    count = 0
    while (count < minHeap.size):
        print("Value is:", minHeap.heap[count])
        count += 1
    minHeap.printHeap()
    # print(minHeap.heap)
