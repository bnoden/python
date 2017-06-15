# 2. File Head Display
# Write a program that asks the user for the name of a file. The program should
# display only the  first  five  lines  of  the  file’s  contents.  If  the
# file  contains  less  than  five  lines,  it  should display the file’s
# entire contents.


def main():
    filename = input("Enter file name: ")   # try numbers.txt
    infile = open(filename, 'r')

    firstfive = ""

    for i in range(5):
        firstfive+=infile.readline()

    infile.close()

    print(firstfive)

main()
