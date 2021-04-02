from helpers import *

from Roster import Roster

from Student import Student 

#Roster
roster = Roster()

while True:
    # Get student information
    first, last, middle, address, email, phone = get_student_information()

    # Create a student
    student = Student(first, last, middle, address, email, phone)

    student.print_info()
    if confirm('Is this information correct? (Y/n) '):
        roster.add(student)

        if confirm('Would you like to input another student\'s information? (Y/n) '):
            continue
        else:
            roster.summarize()
            break
