# Importing the Assignment class from the assingment.py file
from assingment import Assignment

#Created the Homework subclass.
# Homework inherits all the attributes and methods from Assignment.
class Homework(Assignment):
# Constructor for the Homework class.
# It receives the information needed to create a homework assignment.

    def __init__(
            self,
            subject,
            title,
            score,
            max_score,
            due_date
 # Calling the constructor of the parent Assignment class.
# 'homework' is passed as the assignment type.     
    ):
        super().__init__(
             subject,
             title,
             score,
             max_score,
             due_date,
             'homework'

        )