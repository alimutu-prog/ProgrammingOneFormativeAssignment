# Imported the Exam class from the exam module.
from exam import Exam

# Imported the Homework class from the homework module.
from homework import Homework

# Imported the GradeTracker class from the gradetracker module.
from gradetracker import GradeTracker

# Imported the Assignment class from the assignment module.
from assingment import Assignment


# Function used to add a homework or exam assignment.
# 'pot' is the GradeTracker object.
# 'atype' tells the function whether the assignment is homework or an exam.
def add_assingment(pot, atype):

    # Ask the user to enter the subject.
    subject = input("Enter subject: ")

    # Ask the user to enter the assignment title.
    title = input("Enter title: ")

    # Try to convert the score inputs into numbers.
    try:

        # Ask for the score and convert it to a float.
        score = float(input("Enter score: "))

        # Ask for the maximum score and convert it to a float.
        max_score = float(input("Enter maximum score: "))

        # Check that the maximum score is greater than zero,
        # the score is not negative, and the score does not exceed
        # the maximum score.
        if max_score <= 0 or score < 0 or score > max_score:

            # Display an error message if the score is invalid.
            print("Invalid score")

            # Stop the function without adding the assignment.
            return

    # Handle cases where the user enters something that is not a number.
    except ValueError:

        # Tell the user that numbers are required.
        print("Please enter numbers only.")

        # Stop the function.
        return

    # Ask the user to enter the assignment due date.
    due_date = input("Enter due date: ")

    # Check if the assignment type is homework.
    if atype == "homework":

        # Creates a Homework object using the information entered by the user.
        test = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )

    # If the assignment is not homework, create an Exam object.
    else:

        # Creates an Exam object using the information entered by the user.
        test = Exam(
            subject,
            title,
            score,
            max_score,
            due_date
        )

    # Add the newly created assignment to the GradeTracker.
    pot.add_assingment(test)

    # Inform the user that the assignment was successfully added.
    print("Assignment added successfully.")


# Function used to filter assignments.
# It allows the user to filter by type, subject, or month.
def filter_assignments(pot):

    # Display the available filtering options.
    print("\n1. By type (homework/exam)")
    print("2. By subject")
    print("3. By month (YYYY-MM)")

    # Ask the user which filtering option they want to use.
    filter_choice = input("Choose your preferred option: ").strip()

    # Check if the user wants to filter by assignment type.
    if filter_choice == "1":

        # Ask the user to enter homework or exam.
        atype = input("Enter type (homework/exam): ").lower()

        # Get assignments matching the selected type.
        filtered = pot.filter_by_type(atype)

    # Check if the user wants to filter by subject.
    elif filter_choice == "2":

        # Ask the user to enter a subject.
        subject = input("Enter subject: ")

        # Get assignments matching the selected subject.
        filtered = pot.filter_by_subject(subject)

    # Check if the user wants to filter by month.
    elif filter_choice == "3":

        # Ask the user to enter a month in YYYY-MM format.
        month = input("Enter month (YYYY-MM): ")

        # Get assignments matching the selected month.
        filtered = pot.filter_by_month(month)

    # Handle an invalid filtering choice.
    else:

        # Display an error message.
        print("Invalid choice")

        # Create an empty list because no valid filter was selected.
        filtered = []

    # Display the assignments returned by the selected filter.
    pot.list_assingments(filtered)


# Main function that controls the program menu.
def main():

    # Create a GradeTracker object to store the assignments.
    pot = GradeTracker()

    # Keep displaying the menu until the user chooses to exit.
    while True:

        # Display the main menu.
        print("\n1. Add homework")
        print("2. Add exam")
        print("3. List assignments")
        print("4. Filter assignments")
        print("5. Show summary")
        print("0. Exit")

        # Ask the user to select an option.
        choice = input("Enter your choice: ").strip()

        # Option 1: Add a homework assignment.
        if choice == "1":

            # Call the function and specify that the assignment is homework.
            add_assingment(pot, "homework")

        # Option 2: Add an exam.
        elif choice == "2":

            # Call the function and specify that the assignment is an exam.
            add_assingment(pot, "exam")

        # Option 3: List all assignments.
        elif choice == "3":

            # Call the GradeTracker method to display the assignments.
            pot.list_assingments()

        # Option 4: Filter assignments.
        elif choice == "4":

            # Call the filtering function.
            filter_assignments(pot)

        # Option 5: Show the grade summary.
        elif choice == "5":

            # Call the GradeTracker method to display the summary.
            pot.show_grade_summary()

        # Option 0: Exit the program.
        elif choice == "0":

            # Display a goodbye message.
            print("Goodbye")

            # Stop the while loop and end the program.
            break

        # Handle any menu choice that is not recognised.
        else:

            # Tell the user that the selected option is invalid.
            print("Invalid choice")


# Make sure the main function runs only when this file is executed directly.
if __name__ == "__main__":

    # Start the Student Grade/Assignment Tracker.
    main()