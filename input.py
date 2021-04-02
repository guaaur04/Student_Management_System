def get_student_information():
    first = input('Please enter the student\'s first name. ')
    last = input('Please enter the student\'s last name. ')
    middle = input('Please enter the student\'s middle initial. ')
    
    address = input('Please enter the student\'s address. ')
    email = input('Please enter the student\'s email. ')
    phone = input('Please enter the student\'s phone_number. ')

    return [first, last, middle, address, email, phone]