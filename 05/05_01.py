# 1. Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, and then converts that
# distance to miles. The conversion formula is as follows:
# Miles = Kilometers * 0.6214


def k2m(k):
    return k*0.6214

miles = float(input("Enter number of miles: "))
print("{0} miles = {1:.2f} kilometers".format(miles, k2m(miles)))

