class Node:
    def __init__(self, isleaf=False):
        self.keys = []
        self.children = []
        self.isleaf = isleaf


class BTree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def insert(self, key):
        t = self.t
        root = self.root

        # if root is full
        if len(root.keys) == (2 * t) - 1:
            new_root = Node()
            self.root = new_root
            new_root.children.insert(0, root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        t = self.t
        i = len(x.keys) - 1

        # find correct spot in the leaf to insert key
        if x.isleaf:
            x.keys.append(None)
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
            # 30 40 50 50 | 42

        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            # if child is full, split it!
            if len(x.children[i].keys) == (2 * t) - 1:
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], key)

    def split_child(self, x, i):
        t = self.t

        # y is a copy of full x
        y = x.children[i]

        # new node
        z = Node(y.isleaf)
        x.children.insert(i + 1, z)

        x.keys.insert(i, y.keys[t - 1])

        # split apart y's key into y & z
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]

        # reassign the children's of x to y & z
        if not y.isleaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t - 1]

    def print_tree(self, x, level=0):
        print(f'Level {level}', end=': ')

        for i in x.keys:
            print(i, end=" ")

        print()
        level += 1

        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, level)


def insert_example():
    B = BTree(3)

    for i in range(15):
        B.insert(i)

    B.print_tree(B.root)
    print()


def main():
    print('\n--- INSERT ---\n')
    insert_example()


main()
