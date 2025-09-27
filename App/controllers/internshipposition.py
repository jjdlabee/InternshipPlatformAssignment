from App.models import internshipposition
from App.database import db

def create_position(employerID, positionTitle, department, description):
    pos = internshipposition(employerID=employerID, positionTitle=positionTitle, department=department, description=description)
    db.session.add(pos)
    db.session.commit()
    return pos