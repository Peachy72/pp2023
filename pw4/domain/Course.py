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
