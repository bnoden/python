# 4. Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should
# store the numbers in a list and then display the following data:
# •  The lowest number in the list
# •  The highest number in the list
# •  The total of the numbers in the list
# •  The average of the numbers in the list


def main():
    ARRAY_SIZE = 20
    numbers = []
    total = 0

    print("Enter {0} numbers.".format(ARRAY_SIZE))
    for i in range(ARRAY_SIZE):
        numbers.append(int(input("Number {0}: ".format(str(i+1)))))
        total+=numbers[i]

    print("The lowest number is", min(numbers))
    print("The highest number is", max(numbers))
    print("The total is", total)
    print("The average is", total/len(numbers))

main()
