#Student Grade/Assignment Tracker

#Overview

This is a Python command-line program I created to help students keep track of their homework and exam results.
The program allows the user to add assignments, view them, filter them and check their grades. All information is kept in memory while the program is running and is not saved after the program closes.


#Features 
-Add homework and exam assignments
-Enter subject, title, score, maximum score and due date
-List all assignments
-Filter assignments by type, subject, or month
-Calculate the overall average grade
-Calculate averages for each subject
-Show the highest and lowest grades
-Validate scores and user input
-Use OOP with an Assignment class
-Use inheritance with Homework and Exam
-Use a GradeTracker class to manage assignments

#Project Structure

-main.py - Runs the program and menu
-assignment .py - Assignment class
-homework.py - Homework class
-exam.py - Exam class
-gradetracker.py - GradeTracker class
-README.md - Project information
-reflection.pdf - Project reflection

#How to Run
-First, make sure Python 3 is installed.
-Clone the repository and open the project folder in the terminal.
-Run the program with:
-python main.py
-The menu will then appear.


Menu
   STUDENT GRADE/ASSIGNMENT TRACKER
1. Add homework
2. Add exam
3. List assignments
4. Filter assignments
5. Show grade summary
0. Exit

1. Add Homework
The user enters the:
Subject
Assignment title
Score
Maximum score
Due date
The homework is then added to the tracker.
2. Add Exam

The user enters the same information as a homework assignment, but the assignment is stored as an exam.
3. List Assignments
This displays all assignments that have been added during the current session.
4. Filter Assignments
The user can filter assignments by:
Homework or exam
Subject
Month using the YYYY-MM format
5. Show Grade Summary
The program displays:
Overall average grade
Average grade for each subject
Highest scoring assignment
Lowest scoring assignment
0. Exit
Closes the program.







