from .user import create_user
from .student import create_student
from .internshipposition import create_position
from .employer import create_employer
from .staff import create_staff
from .scenario import create_scenario

from App.database import db
from App.models import user, internshipposition, employer, staff


def initialize():
    db.drop_all()
    db.create_all()
    # create_user('bob', 'bobpass')
    # create_student('alice', 'alicepass', 'FST', 'DCIT', 'BSc Comp Sci', 3.5)
    # create_employer('Goodridge', 'Goodpass', 'UWI')
    # create_staff('vj', 'vjpass', 'DCIT')
    create_scenario()
