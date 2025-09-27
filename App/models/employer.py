from App.database import db
from .user import User
from .internshipposition import InternshipPosition

class Employer(User):

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    companyName = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, companyName):
        self.username = username
        self.set_password(password)
        self.companyName = companyName

    def createPosition(self, positionTitle, department, description):
        pos = InternshipPosition(employerID=self.id, positionTitle=positionTitle, department=department, description=description)
        db.session.add(pos)
        db.session.commit()
        return pos

    def createResponse():
        pass