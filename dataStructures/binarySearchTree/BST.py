"""
    Kiana Hosaka
    Implementation of a binary search tree.
"""
from Node import Node

class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        # Returns root of BST
        return self.__root

    def __findNode(self, data):
        """
            Find takes an int and returns the node that holds the value.
            If the node doesn't exist, return null.
        """
        # Top as the top of the tree
        top = self.getRoot()

        # While the top of the tree is not not and data isn't equal to the top of the tree...
        while (top != None and data != top.getData()):
            # Set top as left or right child
            if (data < top.getData()):
                top = top.getLeftChild()
            else:
                top = top.getRightChild()

        return top;

    def exists(self, data):
        """
            Return True if node containing data is present in the tree.
            Otherwise, return False.
        """
        found = self.__findNode(data)

        if (found != None):
            return True
        else:
            return False

    def insert(self, data):
        """
            Find the right spot in the tree for a new node.
        """
        # Create a new node
        node = Node(data)

        # If there is nothing in the tree, the first node inserted becomes the root
        if (self.__root == None):
            self.__root = node
        else:
            # Create two variables to hold the values of the root
            current = self.__root
            parent = self.__root

            # While the current node is not none...
            while (current != None):
                # Set the parent equal to the current
                current.setParent(current)
                parent = current
                
                # Set current node as left or right child
                if current.getData() > data:
                    current = current.getLeftChild()
                else:
                    current = current.getRightChild()

            # Set current and parrent
            current = node
            current.setParent(parent)

            # Set parent's child as left or right child
            if (current.getData() < parent.getData()):
                parent.setLeftChild(current)
            else:
                parent.setRightChild(current)


    def delete(self, data):
        """
            Set variable deleted to contain value of __deleteNode method.
        """
        deleted = self.__deleteNode(self.getRoot(), data)

    def __deleteNode(self, root, data):
        """
            Recurive function to find the node to delete.
        """
        # If the root is none, return the root
        if (root == None):
            return root

        # Set left and right child
        if (data < root.getData()):
            root.setLeftChild(self.__deleteNode(root.getLeftChild(), data))
        elif (data > root.getData()):
            root.setRightChild(self.__deleteNode(root.getRightChild(), data))
        else:
            # If the root's left child is none...
            if (root.getLeftChild() == None):
                current = root.getRightChild()
                root = None
                return current
            # If the root's right child is none...
            elif (root.getRightChild() == None):
                current = root.getLeftChild()
                root = None
                return current

            # Set current value as the successor of the root's right child
            current = self.__findSuccessor(root.getRightChild())

            # Set root's data as current's data
            root.setData(current.getData())

            # Call __deleteNode method on ther right child
            root.setRightChild(self.__deleteNode(root.getRightChild(), current.getData()))

        return root

    def __findSuccessor(self, aNode):
        """
            Find the successor (right once then leftmost node).
        """
        aNode.getRightChild()
        
        while (aNode.getLeftChild() != None):
            aNode = aNode.getLeftChild()

        return aNode

    def traverse(self, order, top):
        """
            Traverse the tree by printing out the node data for all nodes in a specified order.
        """
        if top is not None:
            # Preorder traversal: root, left, right
            if order == "preorder":
                print(top.getData()),
                self.traverse("preorder", top.getLeftChild())
                self.traverse("preorder", top.getRightChild())
            # Inorder traversal: left, root, right
            elif order == "inorder":
                self.traverse("inorder", top.getLeftChild())
                print(top.getData()),
                self.traverse("inorder", top.getRightChild())
            # Postorder traversal: left, right, root
            elif order == "postorder":
                self.traverse("postorder", top.getLeftChild())
                self.traverse("postorder", top.getRightChild())
                print(top.getData()),

            # Error if the order is undefined
            else:
                print("Error, order {} undefined".format(order))
