from domain.Student import Student
from domain.Course import Course
from domain.Mark import Mark
import math

class Input: 
    students = []
    courses = []
    marks = []

    def add_student(students: list):
        print("Adding a student...")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        # check if student already exists
        for student in students:
            if student.id == id:
                print("Student already exists")
                return
        student = Student(student_dob=dob, student_id=id, student_name=name)
        students.append(student)
        print("Student added!")
    
    def add_course(courses: list):
        print("Adding a course...")
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        # check if course already exists
        for course in courses:
            if course.id == id:
                print("Course already exists")
                return
        course = Course(course_id=id, course_name=name)
        courses.append(course)
        print("Course added!")

    def add_mark(marks: list, students: list, courses: list):
        print("Adding a mark...")
        student_id_search = input("Enter student id: ")
        course_id_search = input("Enter course id: ")
        mark = math.floor(float(input("Enter mark: ")))
        selected_student_id = None
        selected_course_id = None

        while True:
            for student in students:
                if student.id == student_id_search:
                    selected_student_id = student_id_search
                    break
                else:
                    selected_course_id = None

            for course in courses:
                if course.id == course_id_search:
                    selected_course_id = course_id_search
                    break
                else:
                    selected_course_id = None

            if selected_student_id is not None and selected_course_id is not None:
                mark = Mark(student_id=student_id_search, course_id=course_id_search, mark=mark)
                marks.append(mark)
                print("Mark added!")
                break

            else:
                if selected_student_id is None:
                    print("Student not found")
                    print("1. Add student and try again")
                    print("2. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        add_student()
                    elif choice == "2":
                        return
                    else:
                        print("Invalid choice")
                        return

                if selected_course_id is None:
                    print("Course not found")
                    print("1. Add course and try again")
                    print("2. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        add_course()
                    elif choice == "2":
                        return
                    else:
                        print("Invalid choice")
                        return