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

# List shortlists by student ID
# @app.cli.command("list_shortlists", help="Lists all shortlists for a student by student ID")
# @click.argument("student_id", default=1)
# def list_shortlists(student_id):
#     student = Student.query.filter_by(id=student_id).first()
#     if student:
#         print(f"Shortlists for Student ID {student_id}:\n")
#         for shortlist in student.shortlists:
#             print(shortlist)
#     else:
#         print(f"No student found with ID {student_id}")

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