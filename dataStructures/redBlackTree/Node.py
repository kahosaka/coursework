"""
    TreeNode is class used to represent nodes in BST.
    Credits: Matthew Hall.
"""

class RB_Node(object):
    def __init__(self, key, left = None, right = None, parent = None, color = 'red'):
        # Can access the variables below directly
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.color = color

    def print_(self):
        print("*"*40)
        print('''
        key     = {}
        parent  = {}
        left    = {}
        right   = {}
        color   = {}
        '''.format(self.key, self.parent.key, self.leftChild.key, self.rightChild.key, self.color))
        print("*"*40)

    def hasLeftChild(self):
        return self.leftChild.parent == self and self.leftChild != self

    def hasRightChild(self):
        return self.rightChild.parent == self and self.rightChild != self

    def isLeftChild(self):
        return self.parent.leftChild == self and self.parent != self

    def isRightChild(self):
        return self.parent.rightChild == self and self.parent != self

    def isRoot(self):
        return self.parent != self and self.parent == self.parent.parent

    def isLeaf(self):
        return not (self.hasLeftChild() or self.hasRightChild())

    def hasOnlyOneChild(self):
        return bool(self.leftChild) ^ bool(self.rightChild)

    def hasAnyChildren(self):
        return bool(self.hasLeftChild() or self.hasRightChild())

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def replaceNodeData(self, key, left = None, right = None, color = 'red'):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        self.color = color

    def findSuccessor(self):
        """
            If node has right child, successor is the min of right subtree.
            If node has no right child but has a parent, node is a left child 
            and successor is the parent.
            If node is a right child and has no right child, remove 
            parent's rightChild reference.
            Call findSuccessor on parent.
            Replace parent's rightChild reference.
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        elif self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
        return succ

    def findMin(self):
        """
            Travels across leftChild of every node and returns node
            that has no leftChild. 
        """
        currentNode = self
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode

    def __iter__(self):
        """
            Defines iterator for objects of RB_node class.
        """
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
