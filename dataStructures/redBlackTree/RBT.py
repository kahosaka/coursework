'''
    Kiana Hosaka
    Implementation of red black trees.
'''
from Node import RB_Node

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0

        # All leaf nodes point to self.sentinel, rather than 'None'
        # Parent of root should also be self.sentinel
        self.sentinel = RB_Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    def sentinel(self):
        return self.sentinel

    def root(self):
        return self.root

    def __iter__(self):
        return self.root.__iter__()

    def getKey(self, key):
        """
            Expects a key and returns key if node is found. Otherwise, KeyError is raised.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.key
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')


    def getNode(self, key):
        """
            Expects a eky, returns RB_Node object for given key.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    def _get(self, key, currentNode):
        """
            Recieves a key and node, returns node with given key.
        """
        if currentNode is self.sentinel:
            print("couldnt find key: {}".format(key))
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get( key, currentNode.leftChild )
        else:
            return self._get( key, currentNode.rightChild )


    def __contains__(self, key):
        """
            Overloads the 'in' operator, allowing for commands.
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        z = self.getNode(key)
        if z.leftChild is self.sentinel or z.rightChild is self.sentinel:
            y = z
        else:
            y = z.findSuccessor()

        if y.leftChild is not self.sentinel:
            x = y.leftChild
        else:
            x = y.rightChild

        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x

        if y is not z:
            z.key = y.key
        
        if y.color == 'black':
            if x is self.sentinel:
                self._rb_Delete_Fixup(y)
            else:
                self._rb_Delete_Fixup(x)

    def traverse(self, order = "in-order", top = -1):
        if top is -1:
            top = self.root
            last_call = True

        last_call = False

        if top is not self.sentinel :
            if order == "in-order":
                self.traverse(order, top.leftChild)
                print(top.key),
                self.traverse(order, top.rightChild)

            if order == "pre-order":
                print(top.key),
                self.traverse(order, top.leftChild)
                self.traverse(order, top.rightChild)

            if order == "post-order":
                self.traverse(order, top.leftChild)
                self.traverse(order, top.rightChild)
                print(top.key),

        if last_call:
            print


    def insert(self, key):
        '''
            Add a key to the tree. Don't forget to fix up the tree ad balance the nodes.
        '''
        # Create new node
        z = RB_Node(key)

        # Set y to be sentinel
        y = self.sentinel

        # Set x to be root
        x = self.root

        # If the root is none, set x to be sentinel
        if (x == None):
            x = self.sentinel

        # While x is not the sentinel...
        while (x != self.sentinel):
            # Sentinel = root
            y = x

            # If z's key is greater than x's key...
            if (z.key < x.key):
                # Make x the left child
                x = x.leftChild
            else:
                # Make x the right child
                x = x.rightChild
        # Make z's parent y
        z.parent = y

        # If y is equal to the sentinel...
        if (y == self.sentinel):
            # Set the root to be z
            self.root = z
        # If z's key is less than y's key...
        elif (z.key < y.key):
            # Set y's left child equal to z
            y.leftChild = z
        else:
            # Else, set y's right child equal to z
            y.rightChild = z
        # Set z's left child to be sentinel
        z.leftChild = self.sentinel

        # Set z's right child to be sentinel
        z.rightChild = self.sentinel

        # Set z's color to be red
        z.color = 'red'

        # Call insert fixup
        self._rbInsertFixup(z)

    def _rbInsertFixup(self, z):
        '''
            Function to balance tree after inserting.
            Less code than delete fixup
        '''
        # While z's parent's color is red...
        while (z.parent.color == 'red'):
            # If z's parent is equal to z's parent's parent's left child...
            if (z.parent == z.parent.parent.leftChild):
                # Make y z's parent's parent's left child
                y = z.parent.parent.rightChild

                # If y's color is red...
                if (y.color == 'red'):
                    # z's parent's color is black
                    z.parent.color = 'black'

                    # Make y's color black
                    y.color = 'black'

                    # Make z's parent's parent's color red
                    z.parent.parent.color = 'red'

                    # Make z its parent's parent
                    z = z.parent.parent
                else:
                    # If z is equal to z's parent's right child...
                    if (z == z.parent.rightChild):
                        # Make z its parent
                        z = z.parent
                        # Call left rotate
                        self.leftRotate(z)
                    # Make z's parent's color black
                    z.parent.color = 'black'
                    # Make z's parent's parent's color red
                    z.parent.parent.color = 'red'
                    #Call right rotate on z's parent's parent
                    self.rightRotate(z.parent.parent)
            else:
                # y is z's parent's parent's left child
                y = z.parent.parent.leftChild

                # If y's color is red...
                if (y.color =='red'):
                    # z's parent's color is black
                    z.parent.color = 'black'
                    # y's parent's color is black
                    y.color = 'black'
                    # z's parent's parent's color is red
                    z.parent.parent.color = 'red'
                    # z is z's parent's parent
                    z = z.parent.parent
                else:
                    # If z is equal to z's parent's left child
                    if(z == z.parent.leftChild):
                        # Make z z's parent
                        z = z.parent
                        # Call right rotate on z
                        self.rightRotate(z)
                    # Make z's parent's color black
                    z.parent.color = 'black'

                    # Make z's parent's parent's color red
                    z.parent.parent.color = 'red'

                    # Call left rotate on z's parent's parent
                    self.leftRotate(z.parent.parent)
        # Make the root's color black
        self.root.color = 'black'


    def _rb_Delete_Fixup(self, x):
        '''
            Recieves a node x and fixes up the tree, balancing from x.
        '''
        # While x is not the root and the color isn't black...
        while (x != self.root and x.color == 'black'):
            # If x is equal to x's parent's left child
            if (x == x.parent.leftChild):
                # temp is x's parent's right child
                temp = x.parent.rightChild
                # Temp might be none, if this is the case break
                if temp.key == None:
                    break
                # If temp's color is red...
                if (temp.color == 'red'):
                    # Make temp's color black
                    temp.color = 'black'
                    # Make x's parent's color red
                    x.parent.color = 'red'
                    # Call left rotate on x's parent
                    self.leftRotate(x.parent)
                    # Make temp x's parent's right child
                    temp = x.parent.rightChild
                # If temp's left child's color is black and temp's right child's color is black...
                if (temp.leftChild.color == 'black' and temp.rightChild.color == 'black'):
                    # Make the temp's color red
                    temp.color = 'red'
                    # Make x x's parent
                    x = x.parent
                # If temp's right child's color is black...
                elif (temp.rightChild.color == 'black'):
                        # Make temp's left child's color black
                        temp.leftChild.color = 'black'
                        # Make temp's color red
                        temp.color = 'red'
                        # Call right rotate on temp
                        self.rightRotate(temp)
                else:
                    # Make temp's color x's parent's color
                    temp.color = x.parent.color
                    # Make x's parent's color is black
                    x.parent.color = 'black'
                    # Make temp's right child's color black
                    temp.rightChild.color = 'black'
                    # Call left rotate on x's parent
                    self.leftRotate(x.parent)
                    # Make x equal to the root
                    x = self.root
            else:
                # Make temp x's parent's left child
                temp = x.parent.leftChild

                # If temp's key is none...
                if temp.key == None:
                    break
                # If temp's color is red...
                if (temp.color == 'red'):
                    # Make temp's color black
                    temp.color = 'black'
                    # Make x's parent's color red
                    x.parent.color = 'red'
                    # Call right rotate on x's parent
                    self.rightRotate(x.parent)
                    # Make temp equal to x's parent's left child
                    temp = x.parent.leftChild
                # If temp's rigth child's color is black and temp's left child's color is black...
                if (temp.rightChild.color == 'black' and temp.leftChild.color == 'black'):
                    # Make temp's color red
                    temp.color = 'red'
                    # Make x x's parent
                    x = x.parent
                # If temp's left child's color is black...
                elif(temp.leftChild.color == 'black'):
                    # Make temp's right child's color black
                    temp.rightChild.color = 'black'
                    # Make temp's color red
                    temp.color = 'red'
                    # Call left rotate on temp
                    self.leftRotate(temp)
                    # Make temp x's parent's left child
                    temp = x.parent.leftChild
                else:
                    # Make temp's color x's parent's color
                    temp.color = x.parent.color
                    # Make x's parent's color black
                    x.parent.color = 'black'
                    # Make temp's left child's color blacks
                    temp.leftChild.color = 'black'
                    # Call right rotate on x's parent
                    self.rightRotate(x.parent)
                    # Make x the root
                    x = self.root
        # Make root's color black
        self.root.color = 'black'

    def leftRotate(self, currentNode):
        '''
            Perform left rotation from given node.
        '''

        # Set the new node to be current node's right child
        newNode = currentNode.rightChild

        # Turn new node's left child into current node's right child
        currentNode.rightChild = newNode.leftChild

        # If new node's left child is not the sentinel...
        if (newNode.leftChild != self.sentinel):
            # Set the current node to be new node's left child's parent
            newNode.leftChild.parent = currentNode

        # Set the new node's parent to be the current node's parent
        newNode.parent = currentNode.parent

        # If the current node's parent is the sentinel...
        if (currentNode.parent == self.sentinel):
            # Make the root the new node
            self.root = newNode
        # If the current node is equal to the current node's parent's left child...
        elif (currentNode == currentNode.parent.leftChild):
            # Set the current node's parent's left child to be the new node
            currentNode.parent.leftChild = newNode
        else:
            # Otherwise set the current node's parent's right child to be the new node
            currentNode.parent.rightChild = newNode

        # Set the new node's left child to be the current node
        newNode.leftChild = currentNode

        # Set the current node's parent to be the new node
        currentNode.parent = newNode


    def rightRotate(self, currentNode):
        '''
            Perform a right rotation from a given node.

        '''
        # Set the new node to be current node's right child
        newNode = currentNode.leftChild

        # Turn new node's right child into current node's left child
        currentNode.leftChild = newNode.rightChild

        # If new node's right child is not equal to self's sentinel
        if (newNode.rightChild != self.sentinel):
            # Make new node's right child's parent the current node
            newNode.rightChild.parent = currentNode
        # Make new node's parent equal to current node's parent
        newNode.parent = currentNode.parent
        # If current node's parent is sentinel...
        if (currentNode.parent == self.sentinel):
            # Make the new node the root
            self.root = newNode
        # If current node is current node's parent's right child...
        elif (currentNode == currentNode.parent.rightChild):
            # Current node's parent's right child is the new node
            currentNode.parent.rightChild = newNode
        else:
            # Current node's parent's left child is the new node
            currentNode.parent.leftChild = newNode
        # New node's right child is current node
        newNode.rightChild = currentNode

        # Current node's parent is new node
        currentNode.parent = newNode

    def search(self, key):
        '''
            Search to search for a key. Returns True or False.
        '''
        return self.__contains__(key)
