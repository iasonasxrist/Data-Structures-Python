class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def  __repr__(self):
        return {self.data, self.next,self.prev}