"""
    Kiana Hosaka
    Max Heap.
"""

class MaxHeap(object):
    def __init__(self, size):
        # Max size is how many can fit, set to size
        self.__maxSize = size

        # Length is how many are contained, set to 0
        self.__length = 0

        # Create a heap with None in the size
        self.__heap = [None] * (size + 1)

    def getHeap(self):
        return self.__heap

    def getLength(self):
        return self.__length

    def setLength(self, l):
        self.__length += 1

    def insert(self, data):
        """
            Insert an element into the heap.
        """
        # Increment length and set data to end
        self.__length += 1
        self.__heap[self.__length] = data

        # i as length
        i = self.__length

        # Get the index of the parent
        parent_i = self.__getParent(self.__length)

        # While i is greater than 1 and value at location i is greater than the parent...
        while ( i > 1 and (self.__heap[i] > self.__heap[parent_i])):
            # Swap the value at location i and the parent then update i and parent
            self.__swap(i, parent_i)
            i = parent_i
            parent_i = self.__getParent(parent_i)

    def maximum(self):
        """
            Return the maximum value in the heap.
        """
        max = self.__heap[1]
        return max


    def extractMax(self):
        """
            Remove and return the maximum value in the heap.
        """
        max = self.__heap[1]

        # Set top value as the last value in heap
        self.__heap[1] = self.__heap[self.__length]

        # Make the last value None
        self.__heap[self.__length] = None # Delete this if causing issues

        # Decrement length
        self.__length -= 1

        # Call heapify to reshape
        self.__heapify(self.__heap[1])

        return max

    def __heapify(self, node):
        """
            Helper function for reshaping the array.
        """

        # Get the node's index, left child, right child
        node_i = self.__getIndex(node)
        left = self.__getLeft(node_i)
        right = self.__getRight(node_i)

        # Set largest 
        if (left <= self.__length and (self.__heap[left] > self.__heap[node_i])):
            largest = left
        else:
            largest = node_i

        if (right <= self.__length and (self.__heap[right] > self.__heap[largest])):
            largest = right

        # If the largest's index is not equal to the node's index swap and call heapify
        if (largest != node_i):
            self.__swap(node_i, largest)
            self.__heapify(self.__heap[1])

    def __swap(self, i, j):
        '''
            Swap x and y.
        '''
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = temp

    def __getIndex(self, node):
        '''
            Returns the index of a node.
        '''
        # For range of 1 to the length...
        for i in range(1, self.getLength() + 1):
            # If the value at location i is equal to the node, return
            if self.__heap[i] == node:
                return i

    def __getParent(self, i):
        '''
            Returns the index of the parent.
        '''
        # Make sure i is greater than or equal to 1, thow error is not
        assert i >= 1

        # If i is equal to 1, return 1 (itself)
        if i == 1:
            return 1
        # Otherwise, return i//2 (parent)
        else:
            return i//2

    def __getLeft(self, i):
        '''
            Returns the left child.
        '''
        return 2 * i

    def __getRight(self, i):
        '''
            Returns the right child.
        '''
        return (2 * i) + 1
