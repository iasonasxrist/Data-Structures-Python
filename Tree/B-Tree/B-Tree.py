class BTreeNode:
    def __init__(self, t, leaf=False) -> None:
        self.isleaf = leaf
        self.keys = [None] * (2 * t-1)
        self.C = [None] * (2 * t)
        self.n = 0
        self.t = t


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def insertNotFull(self, key):
        i = self.n - 1
        if self.isleaf:
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
            self.n += 1
        else:
            # i am intermediate
            while i >= 0 and self.keys[i] > key:
                i -= 1
            if self.C[i + 1].n == (2 * self.t - 1):
                self.splitChild(i + 1, self.C[i + 1])
                if self.keys[i + 1] < key:
                    i += 1
            self.C[i + 1].insertNotFull(key)

    def insert(self, key):
        if self.root == None:
            self.root = BTreeNode(self.t, True)
            self.root.keys[0] = key  # Insert key
            self.root.n = 1
        else:
            if self.root.n == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.C[0] = self.root
                s.splitChild(0, self.root)
                i = 0
                if s.keys[0] < key:
                    i += 1
                    s.C[i].insertNonFull(key)
                self.root = s
            else:
                self.root.insertNonFull(key)

    def splitChild(self, i, y):
        z = BTreeNode(z.t, z.isleaf)
        z.n = self.t - 1 
        # copy t-1 keys from old node to new node
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]

        if not y.isleaf:  # intermediate
            for j in range(self.t):
                z.C[j] = y.C[j + self.t]
        # just copy t-1 childs to new node as a second step
        y.n = self.t - 1
        for j in range(self.n, i, -1):
            self.C[j + 1] = self.C[j]
        # connects parent node with new node
        self.C[i + 1] = z
        for j in range(self.n - 1, i-1, -1):
            self.keys[j + 1] = self.keys[j]
        self.keys[i] = y.keys[self.t - 1]
        self.n += 1

    def traverse(self):
        for i in range(self.n):
            if not self.isleaf:
                self.C[i].traverse()
            print(self.keys[i], end=" ")
        if not self.isleaf:
            self.keysC[i+1].traverse()


if __name__ == '__main__':
    t = BTree(3)  # A B-Tree with minimum degree 3
    t.insert(10)
    t.insert(20)
    t.insert(5)
    t.insert(6)
    t.insert(12)
    t.insert(30)
    t.insert(7)
    t.insert(17)
    print("Traversal of the constructed tree is ", end=' ')
    t.traverse()
    print()
