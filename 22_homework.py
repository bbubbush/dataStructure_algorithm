class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)

        child = len(self.data) - 1
        parent = child // 2
        
        while parent > 0 and self.data[parent] < self.data[child]:
            self.data[parent], self.data[child] = self.data[child], self.data[parent]
            child = parent
            parent = child // 2


def solution(x):
    return 0

heap = MaxHeap()
heap.insert(1)
heap.insert(3)
heap.insert(5)
heap.insert(10)