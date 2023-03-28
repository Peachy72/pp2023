from innput import Input
from ooutput import Output
import math
import os
import zipfile
from domain.Student import Student
from domain.Course import Course
from domain.Mark import Mark
students = []
courses = []
marks = []
gpas = []

def main():
    # unzip file and split into 3 files
    try:
        with zipfile.ZipFile("data.zip", 'r') as zip_ref:
            # extract into current directory
            zip_ref.extractall()
    except:
        print("File not found")
    # check if files exist
    try:
        r = open("students.txt", "r")
        r.close()
        r = open("courses.txt", "r")
        r.close()
        r = open("marks.txt", "r")
        r.close()
    except:
       # open files if they don't exist
        w = open("students.txt", "w")
        w.close()
        w = open("courses.txt", "w")
        w.close()
        w = open("marks.txt", "w")
        w.close()
    # load data from files
    try: 
        r = open("students.txt", "r")
        for line in r.readlines():
            student = line.split()
            # initialize student object
            student = Student(student_id=student[0], student_name=student[1], student_dob=student[2])
            students.append(student)
        r.close()
        r = open("courses.txt", "r")
        for line in r.readlines():
            course = line.split()
            course = Course(course_name=course[1], course_id=course[0])
            courses.append(course)
        r.close()
        r = open("marks.txt", "r")
        for line in r.readlines():
            mark = line.split()
            mark = Mark(student_id=mark[0], course_id=mark[1], mark=mark[2])
            marks.append(mark)
        r.close()
        print("Data loaded successfully")
    except:
        print("Error loading data")
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
            # compress all files into a zip file
            zip_file = zipfile.ZipFile("data.zip", "w")
            zip_file.write("students.txt")
            zip_file.write("courses.txt")
            zip_file.write("marks.txt")
            zip_file.close()
            print("Data compressed")
            # delete all other files
            os.remove("students.txt")
            os.remove("courses.txt")
            os.remove("marks.txt")
            print("Temporary files deleted")
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()