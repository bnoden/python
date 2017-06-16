# 8. Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7,
# Random Number File Writer. Write another program that reads the
# random numbers from the file, display the numbers, and then display
# the following data:
# •  The total of the numbers
# •  The number of random numbers read from the file


def main():
    outfile = open('randomnumbers.txt', 'r')
    line = outfile.readline()
    contents = ""
    total = 0
    count = 0

    while line:
        count+=1
        contents+=line
        total+=int(line)
        line = outfile.readline()

    outfile.close()

    print(contents)
    print("Total:", total)
    print("Count:", count)

main()
