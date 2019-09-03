class MaxHeap:

    def __init__(self):
        self.data = [None]


    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def insert(self, item):
        self.data.append(item)

        child = len(self.data) - 1
        parent = child // 2
        
        while parent > 0 and self.data[parent] < self.data[child]:
            self.data[parent], self.data[child] = self.data[child], self.data[parent]
            child = parent
            parent = child // 2

    def maxHeapify(self, i):
        
        left = i*2
        
        right = i*2+1
        smallest = i
        
        if len(self.data) > left and self.data[left] > self.data[smallest]:
        
            smallest = left
        
        if  len(self.data) > right and self.data[right] > self.data[smallest]:
        
            smallest = right
        if smallest != i:
            # print(self.data)
            # print(smallest)
            # print(i)
            # print(left)
            # print(right)
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
        
            self.maxHeapify(smallest)



def solution(x):
    return 0

heap = MaxHeap()
heap.insert(1)
heap.insert(3)
heap.insert(5)
heap.insert(10)

print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())