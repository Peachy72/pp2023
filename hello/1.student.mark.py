# Student Management System

# Function to input number of students
def input_no_student():
  no_stu = int(input("Number of students: "))
  return no_stu

# Function to input student information with question of id, name and dob
def input_stu_info(no_stu: int):
    stu_info = []
    for i in range(no_stu):
        stu_info.append(input("Student info: ").split())
    return stu_info

# Function to intput number of courses
def input_no_course():
  no_course = int(input("Number of courses: "))
  return no_course

# Function to input course information
def input_course_info(no_course: int):
  course_info = []
  for i in range(no_course):
    course_info.append(input("Course info: ").split())
  return course_info

# Function to select a course, input marks for student in this course
def input_mark(stu_info: list, course_info: list, no_stu: int):
  
  for course in course_info:
    print(course)
  sel = int(input("Select course: "))
  for i in range(no_stu):
    stu_info[i].append(int(input("Grade for student " + str(i+1))))

# Function to list students
def print_stu(list):
  for i in range(len(list)):
    print("ID:" , list[i][0]," Name: ", list[i][1]," DOB: ", list[i][2])

# Function to list courses
def print_course(list):
  for i in range(len(list)):
    print("ID: " , list[i][0]," Name: " , list[i][1])

# Function to show student marks for a given course
def print_mark(stu_info: list, course_info: list):
    for course in course_info:
        print(course)
    sel = int(input("Select course: "))
    for i in range(len(stu_info)):
        print("ID: ", stu_info[i][0]," Name: ", stu_info[i][1]," Grade: ",stu_info[i][sel+2])

#main
no_stu = input_no_student()
stu_info = input_stu_info(no_stu)
no_course = input_no_course()
course_info = input_course_info(no_course)

print("1: Print students\n2:Print courses\n3:Input mark\n4:Print mark\n5:Exit")
while True:
    sel = int(input("Select option: "))
    if sel == 1:
        print_stu(stu_info)
    elif sel == 2:
        print_course(course_info)
    elif sel == 3:
        input_mark(stu_info,course_info,no_stu)
    elif sel == 4:
        print_mark(stu_info,course_info)
    elif sel == 5:
        break
    else:
        print("Invalid selection")

