import main
from main import *

students = []
courses = []
marks = []

def list_students(students: list):
        print("List students")
        print("Id\tName\tDate of birth")
        for student in students:
            print(student.id + "\t" + student.name + "\t" + student.dob)

def list_courses(courses: list):
        print("List courses")
        print("Id\tName")
        for course in courses:
            print(course.id + "\t" + course.name)

def list_marks(marks: list):
    print("List marks")
    print("Student\tCourse\tMark")
    for mark in marks:
        print(mark.get_student_id() , "\t" , mark.get_course_id() , "\t" , mark.get_mark())

def get_gpa(student_id: str, marks: list) -> float:
        total = 0
        count = 0
        for mark in marks:
            count += 1
            if mark.get_student_id() == student_id:
                total += mark.get_mark()
        if count == 0:
            print("Student does not have any marks")
            return 0
        return total / count


def sort_students_by_gpa(students: list, gpas: list):
    for student in students:
        gpas.append(get_gpa(student.id, marks))
    gpas.sort()
    print("ID\tName\tGPA")
    for gpa in gpas:
        for student in students:
            if gpa == get_gpa(student.id, marks):
                print(student.id + "\t" + student.name + "\t" + str(gpa))