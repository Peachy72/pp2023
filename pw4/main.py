import math
import inputt
import output
from inputt import *
from output import *

class Thing(object):
    def __init__(self, name: str, id: str) -> None:
        self._name = name
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id

    @name.setter
    def set_name(self, name) -> None:
        self.name = name
        self._name = "Name is {}".format(name)

    @id.setter
    def set_id(self, id) -> None:
        self.id = id
        self._id = "ID is {}".format(id)

class Student(Thing):
    def __init__(self, student_name: str, student_id: str, student_dob: str) -> None:
        Thing.__init__(self, student_name, student_id)
        self.dob = student_dob

class Course(Thing):
    def __init__(self, course_name: str, course_id: str) -> None:
        Thing.__init__(self, course_name, course_id)


class Mark:
    def __init__(self, student_id: str, course_id: str, mark: int) -> None:
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def get_student_id(self) -> str:
        return self.student_id

    def get_course_id(self) -> str:
        return self.course_id

    def get_mark(self) -> int:
        return self.mark


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
            add_student(students)
            print("hi")
        elif choice == "2":
            add_course(courses)
        elif choice == "3":
            add_mark(marks, students, courses)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            list_marks(marks)
        elif choice == "7":
            student_id = input("Enter student id: ")
            print("Average mark: " + str(get_gpa(student_id, marks)))
        elif choice == "8":
            print("Sort students by GPA")
            gpas.clear()
            sort_students_by_gpa(students, gpas)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()
