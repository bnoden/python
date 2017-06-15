# 5. Sum of Numbers
# Assume that a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk. Write a program that reads all of the
# numbers stored in the file and calculates their total.


def main():
    infile = open("numbers.txt", 'r')
    line = infile.readline()
    sum = 0

    while line:
        sum+=int(line)
        line = infile.readline()

    infile.close()

    print(sum)

main()
