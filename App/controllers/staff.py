from App.models.staff import Staff
from App.database import db

def create_staff(username, password, department):
    sta = Staff(username, password, department)
    db.session.add(sta)
    db.session.commit()
    return sta
    