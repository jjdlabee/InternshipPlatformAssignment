from App.models.employer import Employer
from App.models.staff import Staff
from App.models.student import Student

from App.database import db


def create_scenario():
    emp = Employer('TechCorp', 'techpass', 'Tech Corporation')
    db.session.add(emp)
    db.session.commit()
    pos1 = emp.createPosition('Software Developer Intern', 'IT', 'Assist in software development tasks')
    db.session.add(pos1)
    db.session.commit()
    
    sta = Staff(username='admin', password='adminpass', department='DCIT')
    db.session.add(sta)
    db.session.commit()
    sho1 = sta.createShortlist(1)
    db.session.add(sho1)
    db.session.commit()

    stu = Student(username='john', password='johnpass', faculty='FST', department='DCIT', degree='BSc Comp Sci', gpa=3.8)
    db.session.add(stu)
    db.session.commit()

    sta.addToShortlist(sho1.id, stu.id)
    db.session.add(sta)
    db.session.commit()

    emp.createResponse(pos1.id, stu.id, 'Accepted bro!')
    db.session.add(emp)
    db.session.commit()

