from App.database import db

class InternshipPosition(db.Model):

    __tablename__ = 'internshipposition'

    id = db.Column(db.Integer, primary_key=True)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    positionTitle = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)

    def __init__(self, employerID, positionTitle, department, description):
        self.employerID = employerID
        self.positionTitle = positionTitle
        self.department = department
        self.description = description