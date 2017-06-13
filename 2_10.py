# 10. Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients.
# Write a program that asks the user how many cookies he or she wants to make,
# and then displays the number of cups of each ingredient needed for the
# specified number of cookies.

sugar = 1.5
butter = 1.0
flour = 2.75

cookies = int(input("Enter number of cookies: "))

cookies /= 48
sugar *= cookies
butter *= cookies
flour *= cookies

print("You need: \n"
      "{0} cups of sugar\n"
      "{1} cups of butter\n"
      "{2} cups of flour.".format(sugar, butter, flour))
