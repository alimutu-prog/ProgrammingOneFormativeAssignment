#initialzing parent class#

class Assignment:
    # defining attributes in class assingment #

    def __init__(self,subject,title,score,max_score,due_date,atype):
        self.subject=subject.lower().strip()
        self.title=title
        self.score=float(score)
        self.max_score=float(max_score)
        self.due_date=due_date
        self.atype=atype # 'homework or 'exam' # 

    #creating subclass of assingment#

class Homework(Assignment):
    #accesed attributes of the parent class,atype is not in the init we are alraedy in category of assingment type homework#
    def __init__(self,subject,title,score,max_score,due_date):
        #added sixth attribute from hardcoded compared to above line to avoid bug and respect inheritance rule#
        super().__init__(subject,title,score,max_score,due_date,'homework')
    
    #creating subclass of assingment#

class Exam(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
         super().__init__(subject,title,score,max_score,due_date,'exam')