# 2. Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which rectan-
# gle has the greater area, or if the areas are the same.


def main():
    print("Enter the length and width of two rectangles.")
    r1_len = float(input("Rectangle 1 length: "))
    r1_wid = float(input("Rectangle 1 width: "))
    r2_len = float(input("Rectangle 2 length: "))
    r2_wid = float(input("Rectangle 2 width: "))

    r1_area = r1_len*r1_wid
    r2_area = r2_len*r2_wid

    if r1_area == r2_area:
        print("The rectangles have the same area.")
    elif r1_area > r2_area:
        print("Rectangle 1 is greater.")
    elif r2_area > r1_area:
        print("Rectangle 2 is greater.")

main()
