from App.models.student import Student
from App.models.student import Student_Positions
from App.database import db

def create_student(username, password, faculty, department, degree, gpa):
    stu = Student(username, password, faculty, department, degree, gpa)
    db.session.add(stu)
    db.session.commit()
    return stu

def get_student_by_id(studentID):
    stu = Student.query.filter_by(id=studentID).first()
    if not stu:
        return None
    return stu

def get_student_position(studentID):
    stu = Student_Positions.query.filter_by(id=studentID).first()
    if not stu:
        return None
    return stu.positions

def get_all_students():
    students = Student.query.all()
    if not students:
        return None
    return students