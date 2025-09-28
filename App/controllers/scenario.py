from App.models.employer import Employer
from App.models.staff import Staff
from App.models.student import Student

from App.database import db


def create_scenario():
    emp = Employer('Satoru Iwata', 'iwatapass', 'Nintendo')
    emp2 = Employer('Devon Pritchard', 'devpass', 'Nintendo of America')
    emp3 = Employer('Hidetaka Miyazaki', 'hidepass', 'FromSoftware')
    db.session.add(emp)
    db.session.add(emp2)
    db.session.add(emp3)
    db.session.commit()

    pos1 = emp.createPosition('Software Developer Intern', 'IT', 'Assist in software development tasks')
    pos2 = emp2.createPosition('Game Designer Intern', 'Design', 'Assist in game design tasks')
    pos3 = emp.createPosition('AI Programmer Intern', 'IT', 'Work on AI programming for games')
    db.session.add(pos1)
    db.session.add(pos2)
    db.session.add(pos3)
    db.session.commit()
    
    sta = Staff(username='Masahiro Sakurai', password='smashpass', employerID=emp.id)
    sta2 = Staff(username='Yoshio Sakamoto', password='metropass', employerID=emp.id)
    sta3 = Staff(username='Yoshiaki Koizumi', password='majorapass', employerID=emp.id)
    sta4 = Staff(username='Shigeru Miyamoto', password='mariopass', employerID=emp.id)
    db.session.add(sta)
    db.session.add(sta2)
    db.session.add(sta3)
    db.session.add(sta4)
    db.session.commit()

    stu = Student(username='Naoto Kuroshima', password='streetpass', faculty='FHE', department='DCFA', degree='BSc Visual Arts', gpa=3.8)
    stu2 = Student(username='Eric Barone', password='stardewpassey', faculty='FST', department='DCIT', degree='BSc Comp Sci', gpa=3.9)
    stu3 = Student(username='Toby Fox', password='underpass', faculty='FST', department='DCIT', degree='BSc Comp Sci & Management', gpa=3.7)
    stu4 = Student(username='Milton Guasti', password='m2pass', faculty='FST', department='DCIT', degree='BSc IT', gpa=3.6)
    stu5 = Student(username='Thomas Grip', password='amnepass', faculty='FHE', department='DCFA', degree='BSc Visual Arts', gpa=3.5)
    db.session.add(stu)
    db.session.add(stu2)
    db.session.add(stu3)
    db.session.add(stu4)
    db.session.add(stu5)
    db.session.commit()

    sta.addToShortlist(pos1.id, stu.id)
    sta2.addToShortlist(pos2.id, stu.id)
    db.session.add(sta)
    db.session.commit()

    emp.acceptReject(stu.id, pos1.id, 'accepted', 'Welcome to the team!')
    emp2.acceptReject(stu.id, pos2.id, 'rejected', 'We regret to inform you...')
    db.session.add(emp)
    db.session.commit()

