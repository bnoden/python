# 9. Exception Handling
# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# •  It should handle any IOError exceptions that are raised when the file is opened
# and data is read from it.
# •  It should handle any ValueError exceptions that are raised when the items that
# are read from the file are converted to a number.


def main():
    filename = "numbers.txt"
    infile = open(filename, 'r')
    line = infile.readline()
    total = 0
    count = 0

    while line:
        count+=1
        try:
            total+=int(line)
        except (ValueError):
            ("ERROR: File contains non-numerical values")
        try:
            line = infile.readline()
        except (IOError):
            print("An error occurred while trying to read")
            print("the file", filename)

    infile.close()

    print("Numbers: {0}\n"
          "Sum: {1}\n"
          "Average: {2:.2f}".format(count, total, total/count))


main()
