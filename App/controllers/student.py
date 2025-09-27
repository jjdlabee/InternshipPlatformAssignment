from App.models.student import Student
from App.database import db

def create_student(username, password, faculty, department, degree, gpa):
    stu = Student(username, password, faculty, department, degree, gpa)
    db.session.add(stu)
    db.session.commit()
    return stu