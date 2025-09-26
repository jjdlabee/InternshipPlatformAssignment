from App.database import db
from user import User

class Student(User):

    faculty = db.Column(db.String(20, nullable=False))
    department = db.Column(db.String(20, nullable=False))
    degree = db.Column(db.String(20, nullable=False))
    gpa = db.Column(db.Integer(20, nullable=False))

    def __init__(self, username, password, faculty, department, degree, gpa):
        super().__init__(username, password)
        self.faculty = faculty
        self.department = department
        self.degree = degree
        self.gpa = gpa

    def applyToPosition():
        pass

    def viewShortlist():
        pass

    def viewEmployerResponse():
        pass