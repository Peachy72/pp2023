import math

students = []
courses = []
marks = []
gpas = []

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

    def add_mark( self, marks: list, students: list, courses: list):
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

    # Function to round a number to a given number of decimals
    def rounding(n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    def list_marks( self, marks: list):
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
            return 0
        return Mark.rounding(total / count, 2)

    def sort_students_by_gpa( self, students: list, gpas: list):
        for student in students:
            gpas.append(Mark.get_gpa(student.id))
        gpas.sort()
        print("ID\tName\tGPA")
        for gpa in gpas:
            for student in students:
                if gpa == Mark.get_gpa(student.id):
                    print(student.id + "\t" + student.name + "\t" + str(gpa))
