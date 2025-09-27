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
from App.models.shortlist import Shortlist
# from App.models.student_shortlist import Student_Shortlist
from App.models.employerresponse import EmployerResponse


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
    shortlists = Shortlist.query.all()
    # student_shortlists = Student_Shortlist.query.all()
    responses = EmployerResponse.query.all()
    
    print("")
    
    for emp in employers:
        print(emp.__str__())
    
    print("")
    
    for sta in staff:
        print(sta.__str__())
    
    print("")

    for stu in students:
        print(stu.__str__())
    
    print("")

    for pos in positions:
        print(pos.__str__())
    
    print("")

    for sho in shortlists:
        print(sho.__str__())
    
    # print("")

    # for ss in student_shortlists:
    #     print(ss.__str__())
    
    print("")

    for res in responses:
        print(res.__str__())
    
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