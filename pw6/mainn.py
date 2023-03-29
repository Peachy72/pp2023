from innput import Input
from ooutput import Output
import math
import os
import zipfile
from domain.Student import Student
from domain.Course import Course
from domain.Mark import Mark
import pickle

def pickleData():
    # pickle data
    file = open('database', 'wb')
    pickle.dump({'students': students, 'courses': courses, 'marks': marks}, file)
    file.close()
    # remove temporary files
    if os.path.exists('students.txt'):
        os.remove('students.txt')
    if os.path.exists('courses.txt'):
        os.remove('courses.txt')
    if os.path.exists('marks.txt'):
        os.remove('marks.txt')

def unpickleData():
    file = open('database', 'rb')
    db = pickle.load(file)
    file.close()
    return db

students = []
courses = []
marks = []
gpas = []

def main():
    global students, courses, marks, gpas
    # unpickle data if exists
    if os.path.exists('database'):
        db = unpickleData()
        students = db['students']
        courses = db['courses']
        marks = db['marks']
    while True:
        print(chr(27) + "[2J\n")
        print("Student mark management system\n 1. Add a student\n 2. Add a course\n 3. Add a mark\n 4. List students\n 5. List courses\n 6. List marks\n 7. Get average mark\n 8. Sort students by GPA\n 9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Input.add_student(students)
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
            # pickle data
            pickleData()
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()