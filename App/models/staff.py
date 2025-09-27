from App.database import db
from .user import User
from .shortlist import Shortlist

class Staff(User):
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    department = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, department):
        # super().__init__(username, password)
        self.username = username
        self.set_password(password)
        self.department = department

    def createShortlist(posID):
        shortlist = Shortlist(positionID=posID)
        db.session.add(shortlist)
        db.session.commit()
        return shortlist

    def addToShortlist():
        pass