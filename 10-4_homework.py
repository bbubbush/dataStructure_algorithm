class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def concat(self, L):
        if L.nodeCount != 0:
            self.tail.prev.next = L.head.next
            L.head.next.prev = self.tail.prev

            self.tail = L.tail
            self.nodeCount += L.nodeCount

def solution(x):
    return 0


# Test case
a = Node(1)
b = Node(2)
c = Node(3)
L = DoublyLinkedList()
L2 = DoublyLinkedList()
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)

# a = Node()
# b = Node(5)
# c = Node(6)
# L2.insertAt(1, a)
# L2.insertAt(2, b)
# L2.insertAt(3, c)

print(L.traverse())
print(L2.traverse())
L.concat(L2)
print(L.traverse())