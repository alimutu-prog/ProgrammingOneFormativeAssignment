from exam import Exam
from homework import Homework
from gradetracker import GradeTracker
from assingment import Assignment


pot=GradeTracker()

while True:

    print("\n~~~~~~STUDENT PERFORMANCE TRACKER~~~~")
    print("1.Add homework")
    print("2. exam")
    print("3. List tests")
    print("4. Filter tests")
    print("5. Show grade summary")
    print("0. Exit")

    choice=input("Enter yur choice:").strip()

    if choice == "1":

        subject = input("Enter subject name: ")
        title = input("Enter assingment title: ")

        score = float(input("Enter score: "))
        max_score = float(input("Enter maximum score: "))

        due_date = input(
            "Enter due_date: "
        )

        test = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        pot.add_assingment(test)

        print("Homework assingment added successfully.")

    elif choice == "2":

         subject = input("Enter subject name: ")
         title = input("Enter assingment title: ")
       
         score = float(input("Enter score: "))
         max_score = float(input("Enter maximum score: "))
       
         due_date = input("Enter due_date: ")
       
         test = Exam(
                   subject,
                   title,
                   score,
                   max_score,
                   due_date
               )
       
         pot.add_assingment(test)
       
         print("Exam assingment added successfully.")

    elif choice == "3":

        pot.list_assingments()

    elif choice == "4":

        department = input(
            "Enter assingment type: "
        ).strip()

        filtered = pot.filter_assingments(
            type
        )

        if not filtered:
            print("No assingment of that type  found.")

        else:
            for test in filtered:
                print(test)

    elif choice == "5":

        pot.show_grade_summary()

    elif choice == "0":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")


