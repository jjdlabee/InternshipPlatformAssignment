from App.database import db
from .user import User
from .internshipposition import InternshipPosition
from .employerresponse import EmployerResponse

class Employer(User):

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    companyName = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, companyName):
        self.username = username
        self.set_password(password)
        self.companyName = companyName
    
    def __repr__(self):
        return f"Employer[id= {self.id}, username= {self.username}, companyName= {self.companyName}]"

    def createPosition(self, positionTitle, department, description):
        pos = InternshipPosition(employerID=self.id, positionTitle=positionTitle, department=department, description=description)
        db.session.add(pos)
        db.session.commit()
        return pos

    def createResponse(self, positionID, studentID, message):
        res = EmployerResponse(employerID=self.id, positionID=positionID, studentID=studentID, message=message)
        db.session.add(res)
        db.session.commit()
        return res