# 1. Employee and ProductionWorker Classes
# Write an Employee class that keeps data attributes for the following
# pieces of information:
# •  Employee name
# •  Employee number
# Next, write a class named ProductionWorker that is a subclass of the Employee
# class. The ProductionWorker class should keep data attributes
# for the following information:
# •  Shift number (an integer, such as 1, 2, or 3)
# •  Hourly pay rate
# The  workday  is  divided  into  two  shifts:  day  and  night.  The  shift
# attribute  will  hold  an integer value representing the shift that the employee
# works. The day shift is shift 1 and the night shift is shift 2. Write the
# appropriate accessor and mutator methods for each class.
# Once  you  have  written  the  classes,  write  a  program  that  creates  an
# object  of  the ProductionWorker class and prompts the user to enter data for
# each of the object’s data attributes. Store the data in the object and then use
# the object’s accessor methods to retrieve it and display it on the screen.


class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):

    def __init__(self, name, number):
        Employee.__init__(self, name, number)
        self.__shift = 0
        self.__payrate = 0.0

    def set_shift(self, shift):
        self.__shift = shift

    def set_payrate(self, payrate):
        self.__payrate = payrate

    def get_shift(self):
        return self.__shift

    def get_payrate(self):
        return self.__payrate


def main():

    workername = input("Name: ")
    workernumber = input("ID number: ")
    worker = ProductionWorker(workername, workernumber)

    worker.set_shift(input("Shift (1=day, 2=night): "))
    worker.set_payrate(input("Hourly pay rate: "))

    print("Saving...")
    print("\nThe following information was added to the system:")
    print("Name:", worker.get_name())
    print("ID number:", worker.get_number())
    print("Shift:", worker.get_shift())
    print("Hourly pay rate:", worker.get_payrate())
    print("\nGoodbye.")

main()
