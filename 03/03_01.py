# 1. Day of the Week
# Write  a  program  that  asks  the  user  for  a  number  in  the  range
# of  1  through  7.  The  program should display the corresponding day of
# the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
# 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an
# error message if the user enters a number that is outside the range
# of 1 through 7.

num = 0

while num < 1 or num > 7:
    num = int(input("Enter number between 1 and 7: "))

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
       "Saturday", "Sunday"]

print(day[num-1])

# num = 0
#
# while num < 1 or num > 7:
#     num = int(input("Enter number between 1 and 7: "))
#
# day = ""
#
# if num == 1: day = "Monday"
# elif num == 2: day = "Tuesday"
# elif num == 3: day = "Wednesday"
# elif num == 4: day = "Thursday"
# elif num == 5: day = "Friday"
# elif num == 6: day = "Saturday"
# elif num == 7: day = "Sunday"
#
# print(day)
