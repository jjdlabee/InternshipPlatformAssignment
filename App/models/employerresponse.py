from App.database import db

class EmployerResponse(db.Model):

    responseID = db.Column(db.Integer(20), nullable=False)
    employerID = db.Column(db.Integer(20), nullable=False)
    positionID = db.Column(db.Integer(20), nullable=False)
    message = db.Column(db.String(20), nullable=False)

    def __init__(self):
        super().__init__()