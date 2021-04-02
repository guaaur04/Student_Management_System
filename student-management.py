students = []

while True:

    student = dict.fromkeys(['first_name','last_name','middle_initial','address','email','phone_number'])

    #Prompt user for student's identification information 
    student['first_name'] = input('Please enter the student\'s first name: ')
    student['last_name'] = input('Please enter the student\'s last name: ')
    student['middle_initial'] = input('Please enter the student\'s middle initial: ')

    #Prompt user for student's contact information
    student['address'] = input('Please enter the student\'s address: ')
    student['email'] = input('Please enter the student\'s email: ')
    student['phone_number'] = input('Please enter the student\'s phone number: ')

    #Seperator
    print('-' * 18)

    for key, value in student.items(): print('The student\'s {0}is {1}. '.format(key, value))

    #Seperator 
    print('-' * 18)

    #Confirmation 
    # confirmation = input('Is this information correct?(Y/N) ')

    if input('Is the information correct? (Y/n) ').lower() == 'y' : students.append(student)
    print(students)

    #Prompt user to add more student information 
    if input('Would you like to input another student\'s information? (Y/n)').lower() == 'y':
        continue
    else:
        print('You\'ve enter the following student profiles: ')

        print ('-' * 18)

        for student in students:
            for key, value in student.items():
                print('The student\'s {0} is {1}. '.format(key, value))

        print('-' * 18)

        break