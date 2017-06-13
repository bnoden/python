# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks
# for the price of each item, and then displays the subtotal of the sale,
# the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

tax = 0.07
total = 0.0
numberOfItems = int(input("Enter number of items: "))
count = 0

while numberOfItems:
    count+=1
    total+=float(input("Item {0}: ".format(count)))
    numberOfItems-=1

print("Subtotal: ", format(total, '.2f'))
print("Tax: ", format(total*tax, '.2f'))
print("Total: ", format(total+(total*tax), '.2f'))
