class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev.next == None:
            return None
        else:
            curr = prev.next
            nextNode = curr.next
            prev.next = nextNode
            if prev.next == None:
                self.tail = prev
            # print('head is %s' % self.head.next.data)
            # print('tail is %s' % self.tail.data)
            # print('nodeCount is %s' % self.nodeCount)
            self.nodeCount -= 1
            return curr.data


    def popAt(self, pos):
        #print('head is %s' % self.head.next.data)
        #print('tail is %s' % self.tail.data)
        # print('nodeCount is %s' % self.nodeCount)
        if pos < 1 or pos >= self.nodeCount + 1:
            raise IndexError

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.popAfter(prev)


def solution(x):
    return 0

# Test case
# a = Node(1)
# b = Node(2)
# c = Node(3)
L = LinkedList()
# L.insertAt(1, a)
# L.insertAt(2, b)
# L.insertAt(3, c)

print(L.traverse())
print(L.popAt(1))
# print(L.traverse())
# print(L.popAt(1))
# print(L.traverse())