# Importing the Assignment class from the assingment.py file
from assingment import Assignment


# Created the Exam subclass.
# Exam inherits all the attributes and methods from Assignment.
class exam(Assignment):

# Constructor for the Exam class.
# It receives the information needed to create an exam assignment.
    def __init__(
            self, 
            subject,
            title,
            score,
            max_score,
            due_date):
        
# Calling the constructor of the parent Assignment class.
# 'exam' is passed as the assignment type.
        super().__init__(
            subject,
            title, 
            score, 
            max_score, 
            due_date, 
            'exam')