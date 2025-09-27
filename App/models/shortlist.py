from App.database import db

student_shortlist = db.Table('student_shortlist',
    db.Column('studentID', db.ForeignKey('student.id'), primary_key=True),
    db.Column('shortlistID', db.ForeignKey('shortlist.id'), primary_key=True)
)

class Shortlist(db.Model):

    __tablename__ = 'shortlist'

    id = db.Column(db.Integer, primary_key=True)
    positionID = db.Column(db.Integer, db.ForeignKey('internshipposition.id'), nullable=False)
    students = db.relationship('Student', secondary=student_shortlist, back_populates='shortlists')

    def __init__(self, positionID):
        self.positionID = positionID