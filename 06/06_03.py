# 3. Line Numbers
# Write a program that asks the user for the name of a file. The program should
# display the contents of the file with each line preceded with a line number
# followed by a colon. The line numbering should start at 1.


def main():
    filename = input("Enter file name: ")   # try numbers.txt
    infile = open(filename, 'r')

    line = infile.readline()
    contents = ""
    count = 0

    while line:
        count+=1
        contents+=str(count)+": "+line
        line = infile.readline()

    infile.close()

    print(contents)

main()
