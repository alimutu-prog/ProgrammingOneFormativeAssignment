# Created the GradeTracker class.
# This class is responsible for storing and managing assignments.
class GradeTracker:

# Constructor for the GradeTracker class.
    def __init__(self):
        self.tests=[]

 # Method used to add an assignment to the tracker.
    def add_assingment(self,test):
        self.tests.append(test)

 # Method used to display all assignments.
    def list_assingments(self):

# Check whether the tests list is empty.
        if not self.tests:
            print("\n[!]No tests found.")
            return
# Goes through every test stored in the list.
        for test in self.tests:
            print(test)

# Method used to filter assignments by their type.
# The type can be 'homework' or 'exam'.

    def filter_assingments(self,atype):

# Created a new list containing only assignments
# whose type matches the type entered by the user.
            filtered=[
                test for test in self.tests
                if test.atype.lower()==atype.lower()
            ]

 # Returning the filtered list.
            return filtered

    
def show_grade_summary(self):

    if not self.tests:
        print("\n[!] No tests found. Add entry first")
        return

    def get_percentage(e):
        return (e.score / e.max_score) * 100

    total_percentage = sum(
        get_percentage(e)
        for e in self.tests
    )

    average = total_percentage / len(self.tests)

    high=max(self.tests,key=get_percentage)

    low=min(self.tests,key=get_percentage)



    print("\n" + "=" * 40)
    print("   GRADE SUMMARY")
    print("=" *40)

    print(
        f"overall average grade:"
        f"{average:.1f}%"

    )

    print(
        f"Highest grade:"
        f"{high.subject}"
        f"({get_percentage(high):.1f}%)"
    )


    print(
            f"Lowest grade:"
            f"{low.subject}"
            f"({get_percentage(low):.1f}%)"
        )