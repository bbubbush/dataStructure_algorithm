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


    def insertBefore(self, next, newNode):
        if next.prev == None:
            next.prev = newNode
            newNode.next = next
            self.head.next = newNode
            newNode.prev = self.head
        else:
            prevNode = next.prev
            prevNode.next = newNode
            newNode.next = next
            next.prev = newNode
            newNode.prev = prevNode
        
        self.nodeCount += 1
            
        


def solution(x):
    return 0


# Test case
a = Node(1)
b = Node(2)
c = Node(3)
L = DoublyLinkedList()
L.insertBefore(Node(None), b)
L.insertBefore(b, a)
L.insertBefore(a, c)
print(L.traverse())