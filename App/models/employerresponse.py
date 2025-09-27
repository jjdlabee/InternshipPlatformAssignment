from App.database import db

class EmployerResponse(db.Model):

    __tablename__ = 'employerresponse'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    positionID = db.Column(db.Integer, db.ForeignKey('internshipposition.id'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    message = db.Column(db.String(20), nullable=False)

    def __init__(self, employerID, positionID, studentID, message):
        self.employerID = employerID
        self.positionID = positionID
        self.studentID = studentID
        self.message = message
    
    def __str__(self):
        return f"EmployerResponse[id={self.id}, employerID={self.employerID}, positionID={self.positionID}, studentID={self.studentID}, message={self.message}]"