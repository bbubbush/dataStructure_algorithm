class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if self.key == key:
            raise KeyError
        r = self.key
        
        if r < key:
            if self.right != None:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        elif r > key:
            if self.left != None:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        
            


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0