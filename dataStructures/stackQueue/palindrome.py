"""
    Kiana Hosaka
    Verifying palindromes using stacks and queues.
"""
from sys import argv

class Node(object):
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next

    def setData(self, data):
        self.__data = data

    def setNext(self, next):
        self.__next = next

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next


class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, newData):
        # New node whose data is newData and whose next node is null
        node = Node(newData, None)

        # If it is the first node, both head and tail will be the same node
        if self.__head == None:
            self.__tail = node
            self.__head = node
        else:
            # Update tail and set tail to next node
            self.__tail.setNext(node)
            self.__tail = self.__tail.getNext()

    def dequeue(self):
        # Return null on an empty Queue
        if self.isEmpty() == True:
            return None
        else:
            # Update head with temporary node to hold information
            tmp = self.__head

            # Set head to be the next node
            self.__head = self.__head.getNext()

            # Return the head of the Queue
            return tmp.getData()

    def isEmpty(self):
        # Check if the Queue is empty
        if self.__head == None and self.__tail == None:
            return True
        else:
            return False

    def printQueue(self):
        # Loop through queue and print each Node's data
        # Set the head to current if there is a head
        if self.__head != None:
            cur = self.__head
        else:
            cur = None

        # Print the current head
        while cur != None:
            print(cur.getData())
            cur = cur.getNext()


class Stack(object):
    def __init__(self):
        self.__top = None

    def push(self, newData):
        # New node whose data is newData and next is top
        node = Node(newData, self.__top)

        # If nothing in topp, set to node
        if self.__top == None:
            self.__top = node
        else:
            # Set the next node to be the top and update top
            node.setNext(self.__top) 
            self.__top = node

    def pop(self):
        # Return null on an empty stack
        if self.isEmpty() == True:
            return None
        else:
            # Temporary node to hold information and update top
            tmp = self.__top
            self.__top = self.__top.getNext()

            # Returns the node that currently represents the top of the stack
            return tmp.getData()

    def isEmpty(self):
        # Check if the Stack is empty
        if self.__top == None:
            return True
        else:
            return False

    def printStack(self):
        # Loop through stack and print each Node's data
        # Set the top to current if there is a top
        if self.__top != None:
            cur = self.__top
        else:
            cur = None

        # Print the current top
        while cur != None:
            print(cur.getData())
            cur = cur.getNext()


def main(argv):
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:
        # First input is number of lines in input
        num_line = next(file_ob)

        for line in file_ob:
            # Remove newline characters, spaces, and uppercases
            line = line.strip('\n')
            line = line.replace(" ", "")
            line = line.lower()

            if isPalindrome(line):
                print(line, "is a Palindrome.")
            else:
                print(line, "is not a Palindrome.")


def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack()
    myQueue = Queue()

    # Stack's string is empty and count is 0
    stack_string = ""
    stack_count = 0

    # Queue's string is empty and count is 0
    queue_string = ""
    queue_count = 0

    # For loop to push the strings into stack and update count
    for i in s:
        myStack.push(i)
        stack_count += 1

    # For loop in the range of the count, pop and add to stack's string
    for i in range(stack_count):
        stack_string += myStack.pop()

    # For loop to enqueue the strings into queue and update count
    for i in s:
        myQueue.enqueue(i)
        queue_count += 1

    # For loop in the range of the count, dequeue and add to queue's string
    for i in range(queue_count):
        queue_string += myQueue.dequeue()

    # Checking for equivalency, if they are equivalent return True because it is a palindrome
    # If they are not equivalent, return False because it is not a palindrome
    if(stack_string == queue_string):
        return True
    else:
        return False


if __name__ == "__main__":
    main(argv)
