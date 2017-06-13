# 7. Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
#     MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas
# used. It should calculate the car’s MPG and display the result.

miles = int(input("Miles driven: "))
gas = int(input("Gallons of gas used: "))
mpg = format(miles/gas, '.2f')
print("Your car has {0} miles per gallon".format(mpg))
