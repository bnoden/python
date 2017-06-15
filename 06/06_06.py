# 6. Average of Numbers
# Assume that a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk. Write a program that calculates the
# average of all the numbers stored in the file.


def main():
    infile = open("numbers.txt", 'r')
    line = infile.readline()
    total = 0
    count = 0

    while line:
        count+=1
        total+=int(line)
        line = infile.readline()

    infile.close()

    print("Numbers: {0}\n"
          "Sum: {1}\n"
          "Average: {2:.2f}".format(count, total, total/count))


main()
