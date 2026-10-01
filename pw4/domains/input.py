import math
from domains.student import Student
from domains.course import Course

def round_down(score):
    return math.floor(score *10) /10.0
    
def input_data():
    student = []
    courses = []
    num_s = int(input("input number of students: "))
    for i in range(num_s):
        print(f"input for student {i+1}: ")
        s_id =input("student id: ").strip()
        name = input("student name: ").strip()
        dob =input("student dob: ").strip()
        student.append(Student(s_id,name,dob))

    num_c = int(input("enter number of courses: "))
    for i in range(num_c):
        print(f"enter for course {i+1}")
        c_id = input("course id: ").strip()
        name = input("course name: ").strip()
        credits = int(input("credits: "))
        courses.append(Course(c_id,name,credits))

    print("Enter Marks: ")
    for c in courses: 
        for s in student:
            print(f"enter marks of course: {c.get_name()}:  ")    
            mark = float(input(f"mark for student {s.get_name()}: "))
            mark = round_down(mark)
            s.set_mark(c.get_id(), mark)
    
    for s in student:
        s.caculate_gpa(courses)

    student.sort(key = lambda s: s.get_gpa(), reverse =True)
    return student, courses
