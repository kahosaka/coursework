"""
    Kiana Hosaka
    Main
"""
from sys import argv
from BST import BST

def main(argv):
    input_file = argv[1]

    # Instance of the binary search tree
    tree = BST()

    with open(input_file, 'r') as file_ob:
        for line in file_ob:
            line = line.split()

            if line[0] == 'insert':
                tree.insert(int(line[1]))

            if line[0] == 'delete':
                tree.delete(int(line[1]))

            if line[0] == 'preorder':
                tree.traverse('preorder', tree.getRoot())
                print("")

            if line[0] == 'inorder':
                tree.traverse('inorder', tree.getRoot())
                print("")

            if line[0] == 'postorder':
                tree.traverse('postorder', tree.getRoot())
                print("") 

        # Close the file
        file_ob.close()

if __name__ == "__main__":
    main(argv)
