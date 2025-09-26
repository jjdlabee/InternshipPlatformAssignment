from App.database import db

class Shortlist(db.Model):

    listID = db.Column(db.Integer(20), nullable=False)
    positionID = db.Column(db.Integer(20), nullable=False)
    # students -> array of students

    def __init__(self):
        super().__init__()