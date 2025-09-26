from App.database import db

class Shortlist(db.Model):

    def __init__(self):
        super().__init__()