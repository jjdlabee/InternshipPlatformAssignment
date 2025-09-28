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
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command("list", help="Lists all staff in the database")
def list_staff_command():
    staff = Staff.query.all()
    print("")
    for sta in staff:
        print(sta)
    print("")

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
    positions = InternshipPosition.query.all()
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
        print(f'Student {student.username} added to shortlist of position {position.positionTitle}.')
    else:
        print('Failed to add student to shortlist.')

app.cli.add_command(staff_cli)

'''
Student Commands
'''

student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("list", help="Lists all students in the database")
def list_students_command():
    students = Student.query.all()
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