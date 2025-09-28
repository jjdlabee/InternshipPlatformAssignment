from App.database import db

class Student_Shortlist(db.Model):
    __tablename__ = 'student_shortlist'
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    shortlistID = db.Column(db.Integer, db.ForeignKey('shortlist.id'), primary_key=True)

    def __init__(self, studentID, shortlistID):
        self.studentID = studentID
        self.shortlistID = shortlistID

    def __repr__(self):
        return f"Student_Shortlist[studentID= {self.studentID} -> shortlistID= {self.shortlistID}]"

class Shortlist(db.Model):

    __tablename__ = 'shortlist'

    id = db.Column(db.Integer, primary_key=True)
    positionID = db.Column(db.Integer, db.ForeignKey('internshipposition.id'), nullable=False)
    students = db.relationship('Student', secondary='student_shortlist', back_populates='shortlists')

    def __init__(self, positionID):
        self.positionID = positionID
    
    def __repr__(self):
        return f"Shortlist[id= {self.id}, positionID= {self.positionID}, students= {[student.id for student in self.students]}]"