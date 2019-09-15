'''
    Kiana Hosaka
    CIS 314 Winter 19
'''

from sys import argv
from RBT import RedBlackTree

def main(argv):
    fileName = argv[1]
    T = RedBlackTree()
    with open(fileName, 'r') as fob:
        for line in fob:
            l = line.strip().split()
            if len(l) == 2:
                command = l[0]
                data = int(l[1].strip())
                if command == 'insert':
                    T.insert(data)


                if command == 'delete':
                    T.delete(data)

                # If command is search...
                if command == 'search':
                    # If data exists, print the data
                    if (T.search(data) == True):
                        print(str(data) + ' Found')

            if len(l) == 1:
                print(l[0])
                T.traverse(l[0])
                print('')

    # for i in range(1, 11):
    #     T.insert(i)
    #     T.traverse("pre-order")
    #     print
    #
    # for i in range(1, 11):
    #     T.delete(T.root.key)
    #     T.traverse("pre-order")
    #     print
    #



if __name__ == "__main__":
    main(argv)
