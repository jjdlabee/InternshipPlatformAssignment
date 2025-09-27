from App.database import db

class Shortlist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # positionID = db.Column(db.Integer, db.ForeignKey('internshipposition.positionID'), nullable=False)
    # students -> array of students

    def __init__(self, positionID):
        self.positionID = positionID