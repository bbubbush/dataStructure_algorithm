class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        q = ArrayQueue()
        result = []
        if self.root:
            q.enqueue(self.root)
        while q.isEmpty() == False:
            r = q.dequeue()
            result.append(r.data)
            if r.left != None:
                q.enqueue(r.left)
            if r.right != None:
                q.enqueue(r.right)
            
            
        return result


def solution(x):
    return 0