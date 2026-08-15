#initialzing parent class#

class Assignment:

# Constructor for the Assignment class.
# It receives all the information needed for an assignment.

    def __init__(self,subject,title,score,max_score,due_date,atype):

# Stores the subject.
# lower() converts it to lowercase and strip() removes extra spaces.

        self.subject=subject.strip().lower()

# Store the assignment title.

        self.title=title.strip()

# Convert the score to a floating-point number.

        self.score=float(score)

# Convert the maximum score to a floating-point number.

        self.max_score=float(max_score)

# Store the due date.

        self.due_date=due_date.strip()


# Store the assignment type.
# This will be either 'homework' or 'exam'.

        self.atype=atype.lower() # 'homework or 'exam' #

# __str__() controls how an Assignment object
# is displayed when we use print().

    def __str__(self):

# Return the assignment information as a string.


     return (
        f"{self.subject.title()} | {self.title} | "
        f"{self.score}/{self.max_score} | "
        f"Due: {self.due_date} | {self.atype.title()}"
    )