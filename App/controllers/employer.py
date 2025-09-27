from App.models.employer import Employer
from App.database import db

def create_employer(username, password, companyName):
    emp = Employer(username, password, companyName)
    db.session.add(emp)
    db.session.commit()
    emp.createPosition("Data Entry Clerk", 'Inventory', 'Enter stock data into system')
    db.session.add(emp)
    db.session.commit()
    return emp