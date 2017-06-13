# 1. File Display
# Assume that a file containing a series of integers is named
# numbers.txt and exists on the computer’s disk. Write a
# program that displays all of the numbers in the file.


def main():
    numfile = open("numbers.txt", 'r')
    print(numfile.read())
    numfile.close()

main()
