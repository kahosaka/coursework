"""
    Kiana Hosaka
    Priority queue.
"""

from MaxHeap import MaxHeap

class pQueue(object):
    """
        Priority Queue is like max heap
    """
    def __init__(self,size):
        # Creating a heap
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        self.__myHeap.insert(data)

    def maximum(self):
        return self.__myHeap.maximum()

    def extractMax(self):
        return self.__myHeap.extractMax()

    def isEmpty(self):
        # Return true when the pQueue is empty
        if (self.__myHeap.getLength() <= 1):
            return True
        else:
            return False

    def printQueue(self):
        # Get the heap
        heap = self.__myHeap.getHeap()

        # Empty string
        heap_s = ""

        # For range from 1 to the full length of the heap...
        for i in range(1, self.__myHeap.getLength() + 1):
            # Convert to str and add it to the heap string
            heap_s += str(heap[i])
            # Add a comma after each number
            heap_s += ","

        # Remove the last comma
        result = heap_s.rstrip(',')

        print("Current Queue: " + result)
