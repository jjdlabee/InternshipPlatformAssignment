from App.database import db

class EmployerResponse(db.Model):

    id = db.Column(db.Integer(20), nullable=False, primary_key=True)
    employerID = db.Column(db.Integer(20), db.ForeignKey('employer.id'), nullable=False)
    positionID = db.Column(db.Integer(20), db.ForeignKey('internshipposition.id'), nullable=False)
    message = db.Column(db.String(20), nullable=False)

    def __init__(self, employerID, positionID, message):
        self.employerID = employerID
        self.positionID = positionID
        self.message = message