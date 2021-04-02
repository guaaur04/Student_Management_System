from helpers import *

students = []

while True:
    # Get student information
    first, last, middle, address, email, phone = get_student_information()

    # Create a student
    student = create_student(first_name=first, last_name=last,
                             middle_initial=middle, address=address, email=email,
                             phone_number=phone)

    print_student(student)

    if confirm('Is this information correct? (Y/n) '):
        students.append(student)

        if confirm('Would you like to input another student\'s information? (Y/n) '):
            continue
        else:
            print_summary(students)
            break
