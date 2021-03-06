class Roster:

         def __init__(self):
            self.students = []

         def add(self, student):
            """
            Add a student to the roster.
            """ 
            self.students.append(student)
    
         def summarize(self):
            """
            Print each student's profile information.
            """
            for student in self.students:
                 print('Contact information for {0}. {1} is: '.
                     format(student.first_name[0], student.last_name))
                 student.print_info()
            