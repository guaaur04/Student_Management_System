class Student:

    def __init__(self, first, last, middle, address, email, phone):
        self.first_name = first 
        self.last_name = last 
        self.middle_initial = middle 

        self.address = address
        self.email = email 
        self.phone = phone

    def print_info(self):

        print(self.first_name, self.middle_initial, self.last_name, self.address, "\n", self.email, self.phone)