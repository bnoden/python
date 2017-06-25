# 1. Total Sales
# Design a program that asks the user to enter a store’s sales for each day
# of the week. The amounts should be stored in a list. Use a loop to calculate
# the total sales for the week and display the result.


def main():
    days = ("Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday")
    sales = []
    total = 0

    for i in range(len(days)):
        sales.append(input("Sales for {0}: ".format(days[i])))
        total+=float(sales[i])

    print("Total sales:", total)

main()
