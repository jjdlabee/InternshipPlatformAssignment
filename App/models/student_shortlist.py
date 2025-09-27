from App.models.student import Student
from App.models.shortlist import Shortlist
from App.database import db

class Student_Shortlist(db.Model):

    __tablename__ = 'student_shortlist'

    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False, primary_key=True)
    shortlistID = db.Column(db.Integer, db.ForeignKey('shortlist.id'), nullable=False, primary_key=True)

    def __init__(self, studentID, shortlistID):
        self.studentID = studentID
        self.shortlistID = shortlistID
    
    # def __str__(self):
    #     return f"Student_Shortlist[studentID={self.studentID}, shortlistID={self.shortlistID}]"