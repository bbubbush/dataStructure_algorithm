# -*- coding: utf-8 -*- 
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 0 or pos >= self.nodeCount + 1:
            raise IndexError
        
        if pos == 1:
            currNode = self.head
            self.head = currNode.next
            self.nodeCount -= 1
            if self.nodeCount < 2:
                self.tail = None
            return currNode.data
        elif pos == self.nodeCount:
            prev = self.getAt(pos-1)
            currNode = prev.next
            prev.next = None
            self.tail = prev
            self.nodeCount -= 1
            return currNode.data
        else:
            prevNode = self.getAt(pos-1)
            currNode = prevNode.next
            prevNode.next = currNode.next
            self.nodeCount -= 1
            return currNode.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        print('head is %s' % self.head.data)
        print('tail is %s' % self.tail.data)
        print('nodeCount is %s' % self.nodeCount)
        return result


def solution(x):
    return 0

a = Node(11)
b = Node(22)
c = Node(33)

L = LinkedList()

L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)

print(L.traverse())
print(L.popAt(1))
print(L.traverse())
print(L.popAt(2))
print(L.traverse())
print(L.popAt(1))
print(L.traverse())