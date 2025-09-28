from App.models.staff import Staff
from App.models.student import Student_Position
from App.database import db

def create_staff(username, password, employerID):
    sta = Staff(username, password, employerID)
    db.session.add(sta)
    db.session.commit()
    return sta

def get_staff_by_id(staffID):
    sta = Staff.query.filter_by(id=staffID).first()
    if not sta:
        return None
    return sta

def get_all_staff():
    staffs = Staff.query.all()
    if not staffs:
        return None
    return staffs

# def add_to_shortlist(studentID, positionID):
#     stmt = db.insert(Student_Position).values(studentID=studentID, positionID=positionID, status='pending')

#     db.session.execute(stmt)
#     db.session.commit()
#     return True