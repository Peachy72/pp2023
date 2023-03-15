import math

# Creating class for objects (students/courses)
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

# Student class inherits from Thing class
class Student(Thing):
    def __init__(self, student_name: str, student_id: str, student_dob: str) -> None:
        Thing.__init__(self, student_name, student_id)
        self.dob = student_dob

    def add_student():
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

    def list_students():
        print("List students")
        print("Id\tName\tDate of birth")
        for student in students:
            print(student.id + "\t" + student.name + "\t" + student.dob)

# Course class inherits from Thing class
class Course(Thing):
    def __init__(self, course_name: str, course_id: str) -> None:
        Thing.__init__(self, course_name, course_id)

    def add_course():
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
    
    def list_courses():
        print("List courses")
        print("Id\tName")
        for course in courses:
            print(course.id + "\t" + course.name)


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

    def add_mark():
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

    def list_marks():
        print("List marks")
        print("Student\tCourse\tMark")
        for mark in marks:
            print(mark.get_student_id() , "\t" , mark.get_course_id() , "\t" , mark.get_mark())

    def get_gpa(student_id: str) -> float:
        total = 0
        count = 0
        for mark in marks:
            if mark.get_student_id() == student_id:
                total += mark.get_mark()
                count += 1
        return Mark.rounding(total / count, 2)

    def sort_students_by_gpa():
        for student in students:
            gpas.append(Mark.get_gpa(student.id))
        gpas.sort()
        print("ID\tName\tGPA")
        for gpa in gpas:
            for student in students:
                if gpa == Mark.get_gpa(student.id):
                    print(student.id + "\t" + student.name + "\t" + str(gpa))

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
            Student.add_student()
        elif choice == "2":
            Course.add_course()
        elif choice == "3":
            Mark.add_mark()
        elif choice == "4":
            Student.list_students()
        elif choice == "5":
            Course.list_courses()
        elif choice == "6":
            Mark.list_marks()
        elif choice == "7":
            student_id = input("Enter student id: ")
            print("Average mark: " + str(Mark.get_gpa(student_id)))
        elif choice == "8":
            print("Sort students by GPA")
            gpas.clear()
            Mark.sort_students_by_gpa()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()
