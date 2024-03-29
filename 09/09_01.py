# Write a program that creates a dictionary containing course numbers and the room num-
# bers of the rooms where the courses meet. The dictionary should have the following key-
# value pairs:
# Course Number (key)     Room Number (value)
# CS101                   3004
# CS102                   4501
# CS103                   6755
# NT110                   1244
# CM241                   1411
#
# The program should also create a dictionary containing course numbers and the names of
# the instructors that teach each course. The dictionary should have the following key-value
# pairs:
# Course Number (key)     Instructor (value)
# CS101                   Haynes
# CS102                   Alvarado
# CS103                   Rich
# NT110                   Burke
# CM241                   Lee
#
# The program should also create a dictionary containing course numbers and the meeting
# times of each course. The dictionary should have the following key-value pairs:
# Course Number (key)     Meeting Time (value)
# CS101                   8:00 a.m.
# CS102                   9:00 a.m.
# CS103                   10:00 a.m.
# NT110                   11:00 a.m.
# CM241                   1:00 p.m.
#
# The  program  should  let  the  user  enter  a  course  number,  and  then  it  should  display  the
# course’s room number, instructor, and meeting time.


def main():
    room = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244',
            'CM241': '1411'}
    instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich',
                  'NT110': 'Burke', 'CM241': 'Lee'}
    schedule = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.',
                'NT110': '11:00 a.m.', 'CM241': '1:00 pm'}
    found = 0

    while not found:
        course = input("\nEnter course number: ").upper()
        if ' ' in course:
            course = course.split(' ')
            course = course[0]+course[1]
        if course in room:
            print("Room:", room[course])
            found = 1
        if course in instructor:
            print("Instructor:", instructor[course])
            found = 1
        if course in schedule:
            print("Time:", schedule[course])
            found = 1
        if not found:
            print("Could not find", course)

main()
