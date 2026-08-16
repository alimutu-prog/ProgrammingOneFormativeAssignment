# Creates the GradeTracker class.
# This class is responsible for storing and managing assignments.
class GradeTracker:

    # Constructor for the GradeTracker class.
    # Creates an empty list where assignments will be stored.
    def __init__(self):
        self.tests = []

    # Method used to add an assignment to the tracker.
    # The assignment object is added to the tests list.
    def add_assingment(self, test):
        self.tests.append(test)

    # Method used to display assignments.
    # The 'tests' parameter allows  to display either all assignments
    # or a filtered list of assignments.
    def list_assingments(self, tests=None):

        # If a specific list of tests was provided, use it.
        # Otherwise, use all assignments stored in self.tests.
        items = tests if tests is not None else self.tests

        # Check whether there are any assignments to display.
        if not items:
            print("\nNo assignments to display.\n")
            return

        # Print a line to make the output easier to read.
        print("\n" + "*" * 90)

        # Go through each assignment in the selected list.
        for test in items:

            # Print the assignment using its __str__() method.
            print(test)

        # Print another line after the assignments.
        # Also display the total number of assignments.
        print("*" * 90 + f"\nTotal: {len(items)} assignment(s)\n")

    # Method used to filter assignments by subject.
    def filter_by_subject(self, subject):

        # Remove extra spaces and convert the subject to lowercase.
        subject = subject.strip().lower()

        # Return only assignments whose subject matches the entered subject.
        return [test for test in self.tests if test.subject == subject]

    # Method used to filter assignments by type.
    # The type can be homework or exam.
    def filter_by_type(self, atype):

        # Convert the entered assignment type to lowercase.
        atype = atype.lower()

        # Return only assignments whose type matches the entered type.
        return [test for test in self.tests if test.atype == atype]

    # Method used to filter assignments by month.
    # The month should be entered in YYYY-MM format.
    def filter_by_month(self, month):

        # Return assignments whose due date starts with the given month.
        return [test for test in self.tests if test.due_date.startswith(month)]

    # Method used to display the grade summary.
    def show_grade_summary(self):

        # Check whether there are any assignments stored.
        if not self.tests:
            print("\n[!] No tests found. Add entry first")
            return

        # Function used to calculate the percentage score of an assignment.
        def get_percentage(e):
            return (e.score / e.max_score) * 100

        # Calculate the percentage for every assignment
        # and add all the percentages together.
        total_percentage = sum(get_percentage(e) for e in self.tests)

        # Calculate the overall average percentage.
        average = total_percentage / len(self.tests)

        # Find the assignment with the highest percentage.
        high = max(self.tests, key=get_percentage)

        # Find the assignment with the lowest percentage.
        low = min(self.tests, key=get_percentage)

        # Print the heading for the grade summary.
        print("\n" + "=" * 40)
        print("   GRADE SUMMARY")
        print("=" * 40)

        # Display the overall average grade.
        print(f"Overall average grade: {average:.1f}%")

        # Display the heading for subject averages.
        print("\nPer-subject averages:")

        # Create a sorted set of all subjects in the assignments.
        # The set removes duplicate subjects.
        subjects = sorted(set(test.subject for test in self.tests))

        # Go through each subject.
        for subject in subjects:

            # Get all assignments belonging to the current subject.
            filtered = [test for test in self.tests if test.subject == subject]

            # Add together the scores for that subject.
            subject_score = sum(test.score for test in filtered)

            # Add together the maximum scores for that subject.
            subject_max_score = sum(test.max_score for test in filtered)

            # Calculate the average percentage for the subject.
            subject_average = (subject_score / subject_max_score) * 100

            # Display the subject average.
            print(f"- {subject.title()}: {subject_average:.1f}%")

        # Display the highest scoring assignment.
        print(f"Highest grade: {high.subject.title()} ({get_percentage(high):.1f}%)")

        # Display the lowest scoring assignment.
        print(f"Lowest grade: {low.subject.title()} ({get_percentage(low):.1f}%)")