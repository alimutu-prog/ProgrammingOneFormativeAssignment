from exam import Exam
from homework import Homework
from gradetracker import GradeTracker
from assingment import Assignment


def add_assingment(pot, atype):
    subject = input("Enter subject: ")
    title = input("Enter title: ")

    try:
        score = float(input("Enter score: "))
        max_score = float(input("Enter maximum score: "))

        if max_score <= 0 or score < 0 or score > max_score:
            print("Invalid score")
            return

    except ValueError:
        print("Please enter numbers only.")
        return

    due_date = input("Enter due date: ")

    if atype == "homework":
        test = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )
    else:
        test = Exam(
            subject,
            title,
            score,
            max_score,
            due_date
        )

    pot.add_assingment(test)
    print("Assignment added successfully.")


def filter_assignments(pot):
    print("\n1. By type (homework/exam)")
    print("2. By subject")
    print("3. By month (YYYY-MM)")

    filter_choice = input("Choose your preferred option: ").strip()

    if filter_choice == "1":
        atype = input("Enter type (homework/exam): ").lower()
        filtered = pot.filter_by_type(atype)
    elif filter_choice == "2":
        subject = input("Enter subject: ")
        filtered = pot.filter_by_subject(subject)
    elif filter_choice == "3":
        month = input("Enter month (YYYY-MM): ")
        filtered = pot.filter_by_month(month)
    else:
        print("Invalid choice")
        filtered = []

    if filtered:
        for final in filtered:
            print(final)
    else:
        print("No assignments found.")


def main():
    pot = GradeTracker()

    while True:
        print("\n1. Add homework")
        print("2. Add exam")
        print("3. List assignments")
        print("4. Filter assignments")
        print("5. Show summary")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_assingment(pot, "homework")
        elif choice == "2":
            add_assingment(pot, "exam")
        elif choice == "3":
            pot.list_assingments()
        elif choice == "4":
            filter_assignments(pot)
        elif choice == "5":
            pot.show_grade_summary()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
