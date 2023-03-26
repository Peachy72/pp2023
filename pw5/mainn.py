from innput import Input
from ooutput import Output
import math

students = []
courses = []
marks = []
gpas = []

def main():
    # upon program start, check if students.dat exists
    try:
        r = open("students.dat", "r")
        # if file exists, read file and add students, courses, and marks to their respective lists
        for line in r:
            if line == "Students \n":
                for line in r:
                    if line == "Courses \n":
                        break
                    else:
                        student = Student(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2])
                        students.append(student)
            elif line == "Courses \n":
                for line in r:
                    if line == "Marks \n":
                        break
                    else:
                        course = Course(line.split(" ")[0], line.split(" ")[1])
                        courses.append(course)
            elif line == "Marks \n":
                for line in r:
                    mark = Mark(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2])
                    marks.append(mark)
        r.close()
    except FileNotFoundError:
    # create students.txt 
    w = open("students.txt", "a")
    w.write("ID\tName\tDOB\n")
    w.close()
    # create courses.txt
    w = open("courses.txt", "a")
    w.write("ID\tName\n")
    w.close()
    # create marks.txt
    w = open("marks.txt", "a")
    w.write("Student ID\tCourse ID\tMark\n")
    w.close()
    while True:
        print(chr(27) + "[2J\n")
        print("Student mark management system\n 1. Add a student\n 2. Add a course\n 3. Add a mark\n 4. List students\n 5. List courses\n 6. List marks\n 7. Get average mark\n 8. Sort students by GPA\n 9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Input.add_student(students)
        elif choice == "2":
            w = open("courses.txt", "a")
            w.write("ID\tName\n")
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
            # compress file before exiting program. Compress all files into one file "students.dat"
            w = open("students.dat", "a")
            w.write("Students\n")
            for student in students:
                w.write(student.id + " " + student.name + " " + student.dob + "\n")
            w.write("Courses\n")
            for course in courses:
                w.write(course.id + " " + course.name + "\n")
            w.write("Marks\n")
            for mark in marks:
                w.write(mark.student_id + " " + mark.course_id + " " + str(mark.mark) + "\n")
            w.close()
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()