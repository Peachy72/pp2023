from innput import Input
from ooutput import Output
import math

students = []
courses = []
marks = []
gpas = []

def main():
    while True:
        print(chr(27) + "[2J\n")
        print("Student mark management system\n 1. Add a student\n 2. Add a course\n 3. Add a mark\n 4. List students\n 5. List courses\n 6. List marks\n 7. Get average mark\n 8. Sort students by GPA\n 9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Input.add_student(students)
            print("hi")
        elif choice == "2":
            Input.add_course(courses)
        elif choice == "3":
            Input.add_mark(marks, students, courses)
        elif choice == "4":
            Output.list_students(students)
        elif choice == "5":
            Output.list_courses(courses)
        elif choice == "6":
            Output.list_marks(marks)
        elif choice == "7":
            student_id = input("Enter student id: ")
            print("Average mark: " + str(Output.get_gpa(student_id, marks)))
        elif choice == "8":
            print("Sort students by GPA")
            gpas.clear()
            Output.sort_students_by_gpa(students, gpas, marks)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()