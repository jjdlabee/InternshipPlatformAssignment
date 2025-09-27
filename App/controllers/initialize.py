from .user import create_user
from .internshipposition import create_position
from .employer import create_employer
from .staff import create_staff
from App.database import db
from App.models import user, internshipposition, employer, staff


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    # create_position(1, 'Clerk', 'Inventory', 'Data Entry')
    create_employer('Goodridge', 'Goodpass', 'UWI')
    create_staff('vj', 'vjpass', 'DCIT')
