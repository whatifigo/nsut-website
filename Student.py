from . import db
from models.Faculty import Faculty

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    dept = db.Column(db.String(70))
    guide = db.Column(db.String(15))

    #support constructor with no arguments so that rows can be added from admin panel
    def __init__(self, name="", dept="", guide=""):
        self.name = name
        self.dept = dept
        self.guide = guide

    def __repr__(self):
        return "<Student(name='%s', dept='%s', guide='%s')>" % (
            self.name, self.dept, self.guide)