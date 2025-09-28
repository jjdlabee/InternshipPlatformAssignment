import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )

from App.models.employer import Employer
from App.models.staff import Staff
from App.models.student import Student
from App.models.internshipposition import InternshipPosition
from App.models.student import Student_Position


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

# List command to list all tables in the database
@app.cli.command("list", help="Lists all tables in the database")
def list():
    employers = Employer.query.all()
    staff = Staff.query.all()
    students = Student.query.all()
    positions = InternshipPosition.query.all()
    student_positions = Student_Position.query.all()
    
    print("")
    
    for emp in employers:
        print(emp)
    
    print("")
    
    for sta in staff:
        print(sta)
    
    print("")

    for stu in students:
        print(stu)
    
    print("")

    for pos in positions:
        print(pos)
    
    print("")

    for ss in student_positions:
        print(ss)
    
    print("")


'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Employer Commands
'''

employer_cli = AppGroup('employer', help='Employer object commands')
@employer_cli.command("list", help="Lists all employers in the database")
def list_employers_command():
    employers = Employer.query.all()

    if not employers:
        print("\nNo employers found.\n")
        return

    print("")
    for emp in employers:
        print(emp)
    print("")

app.cli.add_command(employer_cli)

@employer_cli.command("view-positions", help="View positions for a specified employer")
def view_positions_command():
    print("\nEmployers:\n")
    employers = Employer.query.all()
    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    print("")
    emp = Employer.query.filter_by(id=empID).first()
    if not emp:
        print('Employer not found.')
        return

    positions = InternshipPosition.query.filter_by(employerID=empID).all()
    if positions:
        for pos in positions:
            print(pos)
    else:
        print('No positions found for this employer.')
    print("")

@employer_cli.command("view-position-shortlist", help="View the shortlist for a specified position")
def view_position_shortlist_command():

    print("\nEmployers:\n")
    employers = Employer.query.all()
    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    print("")
    emp = Employer.query.filter_by(id=empID).first()
    if not emp:
        print('Employer not found.')
        return

    print("\nPositions:\n")
    positions = InternshipPosition.query.filter_by(employerID=empID).all()
    for pos in positions:
        print(f'Position ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    print("")
    position = InternshipPosition.query.filter_by(id=position_id).first()
    if not position:
        print('Position not found.')
        return

    student_positions = Student_Position.query.filter_by(positionID=position_id).all()
    if student_positions:
        for sp in student_positions:
            print(sp)
    else:
        print('No students found in the shortlist for this position.')
    print("")

@employer_cli.command("create", help="Creates an employer")
def create_employer_command():
    username = input('\nEnter employer username: ')
    password = input('\nEnter employer password: ')
    companyName = input('\nEnter company name: ')

    e = Employer.query.filter_by(username=username, companyName=companyName).first()
    if e:
        print('\nThis employer already exists.')
        return
    else:
        print('Creating new employer...')
        emp = Employer(username, password, companyName)
        db.session.add(emp)
        db.session.commit()
        print(f'Employer {username} created!')

@employer_cli.command("create-position", help="Create a new internship position")
def create_position_command():
    print("\nEmployers:\n")
    employers = Employer.query.all()
    print("")
    for emp in employers:
        print(f'ID: {emp.id} | Name: {emp.username} | Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = Employer.query.filter_by(id=empID).first()
    if not emp:
        print('Employer not found.')
        return

    title = input('\nEnter position title: ')
    depart = input('\nEnter department: ')
    descr = input('\nEnter description: ')

    p = InternshipPosition.query.filter_by(positionTitle=title, employerID=empID, department=depart, description=descr).first()
    if p:
        inp = ""
        print('This position already exists for this employer. Would you like to create a duplicate? (y/n): ')

        while inp not in ['y', 'n']:
            inp = input().lower()
            if inp not in ['y', 'n']:
                print('Invalid input. Please enter "y" or "n".')
        if inp == 'n': 
            print('Position creation cancelled.')
            return

    position = emp.createPosition(title, depart, descr)
    db.session.add(position)
    db.session.commit()
    print(f'"{position.positionTitle}" position created for employer {emp.username}.')

@employer_cli.command("accept-reject", help="Accept or reject a student application")
def accept_reject_command():
    print("\nEmployers:\n")
    employers = Employer.query.all()
    print("")
    for emp in employers:
        print(f'ID: {emp.id} | Name: {emp.username} | Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = Employer.query.filter_by(id=empID).first()
    if not emp:
        print('Employer not found.')
        return
    
    # Should close positions after a person is accepted, but for simplicity we will not implement that here

    print("\nPositions:\n")
    positions = InternshipPosition.query.filter_by(employerID=empID).all()
    for pos in positions:
        print(f'ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    position = InternshipPosition.query.filter_by(id=position_id).first()
    if not position:
        print('Position not found.')
        return

    print("\nStudents who applied to this position:\n")
    student_positions = Student_Position.query.filter_by(positionID=position_id).all()
    for sp in student_positions:
        student = Student.query.filter_by(id=sp.studentID).first()
        print(f'ID: {student.id} Name: {student.username} Status: {sp.status}')
    
    student_id = input('\nEnter student ID: ')
    sp = Student_Position.query.filter_by(studentID=student_id, positionID=position_id).first()
    if not sp:
        print('This student did not apply to this position.')
        return

    status = input('\nEnter new status (accepted/rejected): ').lower()
    while status not in ['accepted', 'rejected']:
        print('Invalid status. Please enter "accepted" or "rejected".')
        status = input('\nEnter new status (accepted/rejected): ').lower()

    message = input('\nEnter an optional message (press Enter to skip): ')
    if message.strip() == '':
        message = None

    if emp.acceptReject(student_id, position_id, status, message):
        print(f'Student application updated to "{status}".')
    else:
        print('Failed to update application status.')

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command("list", help="Lists all staff in the database")
def list_staff_command():
    staff = Staff.query.all()

    if not staff:
        print("\nNo staff found.\n")
        return

    print("")
    for sta in staff:
        print(sta)
    print("")

@staff_cli.command("create", help="Creates a staff member")
def create_staff_command():
    print("\nEmployers:\n")
    employers = Employer.query.all()
    print("Select an employer to associate with the new staff member:\n")
    for emp in employers:
        print(f'ID: {emp.id} Name: {emp.username} Company: {emp.companyName}')
    
    empID = input('\nEnter employer ID: ')
    emp = Employer.query.filter_by(id=empID).first()
    if not emp:
        print('Employer not found.')
        return

    username = input('\nEnter staff username: ')
    password = input('\nEnter staff password: ')

    s = Staff.query.filter_by(username=username, employerID=emp.id).first()
    if s:
        print('\nThis staff member already exists for this employer.')
        return

    sta = Staff(username, password, emp.id)
    db.session.add(sta)
    db.session.commit()
    print(f'Staff member {username} created for employer {emp.username}.')

@staff_cli.command("add-to-shortlist", help="Add a student to a position's shortlist")
def add_to_shortlist_command():
    print("\nStaff:\n")
    staff = Staff.query.all()
    print("")
    for sta in staff:
        print(f'ID: {sta.id} Name: {sta.username}')
    
    staff_id = input('\nEnter staff ID: ')
    print("")
    staff = Staff.query.filter_by(id=staff_id).first()
    if not staff:
        print('Staff not found.')
        return

    print("\nPositions:\n")
    positions = InternshipPosition.query.filter_by(employerID=staff.employerID).all()
    if not positions:
        print('No positions found for the employer associated with this staff member.')
        return
    for pos in positions:
        print(f'ID: {pos.id} Title: {pos.positionTitle}')
    
    position_id = input('\nEnter position ID: ')
    position = InternshipPosition.query.filter_by(id=position_id).first()
    if not position:
        print('Position not found.')
        return

    print("\nStudents:\n")
    students = Student.query.all()
    for stu in students:
        print(f'ID: {stu.id} Name: {stu.username}')
    
    student_id = input('\nEnter student ID: ')
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        print('Student not found.')
        return

    sp = Student_Position.query.filter_by(studentID=student_id, positionID=position_id).first()
    if sp:
        print('Student is already in the shortlist for this position.')
        return

    if staff.addToShortlist(position_id, student_id):
        print(f'\nStudent {student.username} added to shortlist of position {position.positionTitle}.')
    else:
        print('\nFailed to add student to shortlist.')

app.cli.add_command(staff_cli)

'''
Student Commands
'''

student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("list", help="Lists all students in the database")
def list_students_command():
    students = Student.query.all()

    if not students:
        print("\nNo students found.\n")
        return

    print("")
    for stu in students:
        print(stu)
    print("")

@student_cli.command("view-shortlists", help="View shortlists a specified student was added to")
def view_shortlists_command():
    print("\nStudents:\n")
    students = Student.query.all()
    for stu in students:
        print(f'ID: {stu.id} Name: {stu.username}')
    
    student_id = input('\nEnter student ID: ')
    print("")
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        print('Student not found.')
        return

    student = Student_Position.query.filter_by(studentID=student_id).all()
    if student:
        for s in student:
            print(s)
    else:
        print('No shortlists found for this student.')
    print("")

app.cli.add_command(student_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)