#Prompt user for student's identification information 
first_name = input('Please enter the student\'s first name: ')
last_name = input('Please enter the student\'s last name: ')
middle_initial = input('Please enter the student\'s middle initial: ')

#Prompt user for student's contact information
address = input('Please enter the student\'s address: ')
email = input('Please enter the student\'s email: ')
phone_number = input('Please enter the student\'s phone number: ')

#Seperator
print('-' * 18)

#Print everything to the console 

print('The student\'s first name is {0}'.format(first_name))
print('The student\'s last name is {0}'.format(last_name))
print('The student\'s middle initial is {0}'.format(middle_initial))

print('The student\'s address is {0}'.format(address))
print('The student\'s email is {0}'.format(email))
print('The student\'s phone number is {0}'.format(phone_number))

#Seperator 
print('-' * 18)

#Confirmation 
confirmation = input('Is this information correct?(Y/N) ')