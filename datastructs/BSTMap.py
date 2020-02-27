class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.key}: {self.value}'

class BSTMap:
    def __init__(self):
        self.size = 0
        self.root = None
        pass

    def size(self):
        pass

    def add(self):
        pass

    def contains(self):
        pass

    def remove(self):
        pass

    def __repr__(self):
        if self.root is None:
           return ""
        else:
            self.printRec(self.root)

    def printRec(self, mRoot: BSTNode):
       if mRoot:
           self.printRec(mRoot.left);
           print("key -> ", mRoot.key, ": ", "value -> ", mRoot.value)
           self.printRec(mRoot.right)


if __name__ == "__main__":
    print("testing the map")
    num = BSTNode(10, None)
    print(num)
