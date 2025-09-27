from App.database import db
from .user import User
from .shortlist import Shortlist
from .student import Student

from sqlalchemy import select

class Staff(User):
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    department = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, department):
        self.username = username
        self.set_password(password)
        self.department = department

    def __str__(self):
        return f"Staff[id={self.id}, username={self.username}, department={self.department}]"

    def createShortlist(self, posID):
        shortlist = Shortlist(positionID=posID)
        db.session.add(shortlist)
        db.session.commit()
        return shortlist

    def addToShortlist(self, shortlistID, studentID):
        
        shortlist = Shortlist.query.filter_by(id=shortlistID).first()

        student = Student.query.filter_by(id=studentID).first()

        if shortlist != None and student != None:
            shortlist.students.append(student)
            db.session.commit()
            return True

        return False