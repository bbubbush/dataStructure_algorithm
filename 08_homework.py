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
        
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            
        if pos == 1:
            result = None
                
            result = self.head.data
            
            self.head = self.head.next
            self.nodeCount -= 1
            if self.nodeCount < 2:
                self.tail = None
            print("head 11is {}".format(self.head.data))
            print("tail 11is {}".format(self.tail.data))
            print("nodeCount 11is {}".format(self.nodeCount))
            return result
        else:
            if pos == self.nodeCount:
                self.tail = self.getAt(pos-1)    
            prev = self.getAt(pos-1)
            target = prev.next
            if target.next != None:
                prev.next = target.next
            else:
                prev.next = None
            self.nodeCount -= 1
            if self.nodeCount == 1:
                self.tail = None
            print("head 22is {}".format(self.head.data))
            print("tail 22is {}".format(self.tail.data))
            print("nodeCount 22is {}".format(self.nodeCount))
            return target.data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
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

print(L.popAt(2))
print(L.popAt(2))
print(L.popAt(1))