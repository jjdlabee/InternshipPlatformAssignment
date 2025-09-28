from App.models.staff import Staff
from App.database import db

def create_staff(username, password, employerID):
    sta = Staff(username, password, employerID)
    db.session.add(sta)
    db.session.commit()
    sta.createShortlist(1)
    db.session.add(sta)
    db.session.commit()
    return sta
    