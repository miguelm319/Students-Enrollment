class Student:
    def __init__(self, students_id, first_name, last_name, email):
        self.students_id = students_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Course:
    def __init__(self, course_id, course_code, course_name):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id        