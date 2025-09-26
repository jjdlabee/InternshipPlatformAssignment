from App.database import db
from user import User

class Staff(User):
    
    department = db.Column(db.String(20, nullable=False))

    def __init__(self, username, password):
        super().__init__(username, password)

    def createShortlist():
        pass

    def addToShortlist():
        pass