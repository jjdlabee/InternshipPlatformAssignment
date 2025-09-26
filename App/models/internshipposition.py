from App.database import db

class InternshipPosition(db.Model):

    positionID = db.Column(db.Integer(20), nullable=False)
    employerID = db.Column(db.Integer(20), nullable=False)
    positionTitle = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)

    def __init__(self, employerID, positionTitle, department, description):
        super().__init__()
        self.employerID = employerID
        self.positionTitle = positionTitle
        self.department = department
        self.description = description