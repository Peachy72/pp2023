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

