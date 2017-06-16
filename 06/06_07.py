# 7. Random Number File Writer
# Write  a  program  that  writes  a  series  of  random  numbers  to  a  file.
# Each  random  number should be in the range of 1 through 500. The application
# should let the user specify how many random numbers the file will hold.
import random


def main():
    howmany = int(input("How many random numbers would you like the file to hold? "))
    outfile = open('randomnumbers.txt', 'w')

    for i in range(howmany):
        outfile.write(str(random.randint(1, 500))+'\n')

    outfile.close()
    print("{0} random numbers written to file.".format(howmany))

main()
