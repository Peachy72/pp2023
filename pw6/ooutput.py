from innput import Input
from domain.Mark import Mark

class Output:
    def list_students(students: list):
        print("List students")
        print("Id\tName\tDate of birth")
        for student in students:
            print(student.id + "\t" + student.name + "\t" + student.dob)
        
    def list_courses(courses : list):
        print("List courses")
        print("Id\tName")
        for course in courses:
            print(course.id + "\t" + course.name)

    # Function to round a number to a given number of decimals
    def rounding(n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    def list_marks(marks: list):
        print("List marks")
        print("Student\tCourse\tMark")
        for mark in marks:
            print(mark.get_student_id() , "\t" , mark.get_course_id() , "\t" , mark.get_mark())

    def get_gpa(student_id: str, marks: list) -> float:
        total = 0
        count = 0
        for mark in marks:
            if mark.get_student_id() == student_id:
                total += mark.get_mark()
                count += 1
        if count == 0:
            print("Student has no marks")
            return 0

        return Mark.rounding(total / count, 2)

    def sort_students_by_gpa(students: list, gpas: list, marks: list):
        for student in students:
            gpas.append(Mark.get_gpa(student.id, marks))
        gpas.sort()
        print("ID\tName\tGPA")
        for gpa in gpas:
            for student in students:
                if gpa == Mark.get_gpa(student.id, marks):
                    print(student.id + "\t" + student.name + "\t" + str(gpa))
