# 4. Item Counter
# Assume that a file containing a series of names (as strings) is named
# names.txt and exists on the computer’s disk. Write a program that displays
# the number of names that are stored in the file.
# (Hint: Open the file and read every string stored in it. Use a variable to keep a
# count of the number of items that are read from the file.)


def main():
    namesfile = "names.txt"
    infile = open(namesfile, 'r')
    line = infile.readline()
    count = 0

    while line:
        count+=1
        line = infile.readline()

    print("There are {0} names found in {1}".format(str(count), namesfile))

main()
