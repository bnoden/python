# 1. Initials
# Write  a  program  that  gets  a  string  containing  a  person’s  first,
# middle, and  last  names, and then display their first, middle, and last
# initials. For example, if the user enters John William Smith the program
# should display J. W. S.


def main():
    name = input("Enter full name (first middle last): ")
    namesplit = name.split(' ')
    initials = namesplit[0][0]+". "+namesplit[1][0]+". "+namesplit[2][0]+". "

    print("Your initials are", initials)

main()
