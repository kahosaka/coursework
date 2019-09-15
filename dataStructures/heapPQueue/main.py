"""
    Kiana Hosaka
    Main
"""

from sys import argv
from pQueue import pQueue

def main(argv):
    # Input file will be the second argument
    inputFile = argv[1]

    # Number of lines is currently 0
    num_lines = 0

    # Open the file to get the max size
    with open(inputFile, 'r') as file_ob:
        # Loop over input file
        for line in file_ob:

            # Split each line
            line = line.split()

            # If the instruction is to insert, count how many inserts there are
            if line[0] == 'insert':
                num_lines += 1

    # Create an instance of pQueue
    mypQueue = pQueue(num_lines)

    # Open the file again
    with open(inputFile, 'r') as file_ob:
        # Loop over input file
        for line in file_ob:

            # Split each line
            line = line.split()

            # If the instruction is to insert...
            if line[0] == 'insert':
                # Convert str to int and insert
                mypQueue.insert(int(line[1]))

            # If the instruction is to print, print the pQueue
            if line[0] == 'print':
                mypQueue.printQueue()

            # If the instruction is checking if the pQueue is empty...
            if line[0] == 'isEmpty':
                # If the pQueue is not empty, print 'Not Empty'
                if (mypQueue.isEmpty() != True):
                    print('Not Empty')
                else:
                    print('Empty')

            # if the instruction is to get the maximum, print the maximum
            if line[0] == 'maximum':
                print(mypQueue.maximum())

            # If the instruction is to extract the max, extract the maximum value and print
            if line[0] == 'extractMax':
                print(mypQueue.extractMax())

    # Close the file
    file_ob.close()

if __name__ == "__main__":
    main(argv)
