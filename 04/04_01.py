# 1. Bug Collector
# A bug collector collects bugs every day for five days. Write a program that
# keeps a running total  of  the  number  of  bugs  collected  during  the
# five  days.  The  loop  should  ask  for  the number of bugs collected for
# each day, and when the loop is finished, the program should
# display the total number of bugs collected.

bugs = 0

for days in range(1, 6):
    bugs += int(input("Bugs collected on day {0}: ".format(days)))

print("\nTotal bugs collected: {0}".format(bugs))
