from App.database import db
from App.models.user import User

class Student(User):

    __tablename__ = 'student'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    faculty = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    degree = db.Column(db.String(20), nullable=False)
    gpa = db.Column(db.Integer, nullable=False)
    shortlists = db.relationship('Shortlist', secondary='student_shortlist', back_populates='students')

    def __init__(self, username, password, faculty, department, degree, gpa):
        self.username = username
        self.set_password(password)
        self.faculty = faculty
        self.department = department
        self.degree = degree
        self.gpa = gpa

    def __repr__(self):
        return f"Student[id= {self.id}, username= {self.username}, faculty= {self.faculty}, department= {self.department}, degree= {self.degree}, gpa= {self.gpa}]"

    def viewShortlist():
        pass

    def viewEmployerResponse():
        pass