class MinHeap:
    def __init__(self):
        self.data = [None]

    def isEmpty(self):
        return len(self.data) < 2

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.minHeapify(1)
        else:
            data = None
        return data

    def insert(self, item):
        self.data.append(item)

        child = len(self.data) - 1
        parent = child // 2
        
        while parent > 0 and self.data[parent] > self.data[child]:
            self.data[parent], self.data[child] = self.data[child], self.data[parent]
            child = parent
            parent = child // 2

    def minHeapify(self, i):
        left = i*2
        right = i*2+1
        biggest = i
        
        if len(self.data) > left and self.data[left] < self.data[biggest]:
        
            biggest = left
        
        if  len(self.data) > right and self.data[right] < self.data[biggest]:
        
            biggest = right
        if biggest != i:
            self.data[i], self.data[biggest] = self.data[biggest], self.data[i]
        
            self.minHeapify(biggest)

class MaxHeap:
    def __init__(self):
        self.data = [None]

    def isEmpty(self):
        return len(self.data) < 2

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
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)


class HeapSort:
    def __init__(self):
        self.heap = None
    
    def sort(self, arr, isDescending = False):
        if isDescending:
            self.heap = MaxHeap()
        else:
            self.heap = MinHeap()
        
        result = []
        # insert to heap
        if len(arr) > 0:
            for data in arr:
                self.heap.insert(data)
            while self.heap.isEmpty() == False:
                result.append(self.heap.remove())
            return result
        else:
            return arr

        




def solution(x):
    return 0

s = HeapSort()
paramArr = [3, 6, 10, 2, 9, 0]
print(s.sort(paramArr, True))
print(s.sort(paramArr, False))
# heap = MinHeap()
# heap.insert(1)
# heap.insert(3)
# heap.insert(5)
# heap.insert(10)

# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())