from . import db
from datetime import datetime
'''
from hashlib import md5
from flask.ext.login import LoginManager, current_user, login_user, logout_user

login_manager = LoginManager()
login_manager.login_view =  "login"

@login_manager.user_loader
def load_user(fid):
        return Faculty.query.filter_by(faculty_id=fid).first()
'''
class Faculty(db.Model):
    __tablename__ = 'faculties'
    faculty_id = db.Column(db.String(15), primary_key=True)
    title = db.Column(db.String(15))
    name = db.Column(db.String(50))
    dept = db.Column(db.String(70))
    email_id = db.Column(db.String(100))
    designation = db.Column(db.String(75))
    photo = db.Column(db.String(500))
    # bio = db.Column(db.String(10000))
    bio = db.Column(db.Text)
    publications = db.Column(db.Text)
    qualification = db.Column(db.String(100))
    honours_and_awards = db.Column(db.Text)
    contact = db.Column(db.String(80))
    # interests = db.Column(db.String(2000))
    interests = db.Column(db.Text)
    rank = db.Column(db.Integer)
    '''
    subjects_odd = db.Column(db.String(2000))
    subjects_even = db.Column(db.String(2000))
    password = db.Column(db.String(50))
    '''

    #support constructor with no arguments so that rows can be added from admin panel
    def __init__(self, faculty_id="", title="", name="", dept="", 
                email_id="", designation="", photo="", bio="", publications="", 
                qualification="", honours_and_awards="", contact="", interests=""):#, subjects_odd="",
                #subjects_even="", password=""):
        self.faculty_id = faculty_id
        self.title = title
        self.name = name
        self.dept = dept
        self.email_id = email_id
        self.designation = designation
        self.photo = photo
        self.bio = bio
        self.publications = publications
        self.qualification = qualification
        self.honours_and_awards = honours_and_awards
        self.contact = contact
        self.interests = interests
        '''
        self.subjects_odd = subjects_odd
        self.subjects_even = subjects_even
        self.password = md5(str(password)).hexdigest()
        '''
    def __repr__(self):
        return "<Faculty(faculty_id='%s',title='%s' ,name='%s', dept='%s', email_id='%s', designation='%s', photo='%s', bio='%s', publications='%s', qualification='%s', honours_and_awards='%s', contact='%s', interests='%s')>" % (
            self.faculty_id, self.title, self.name, self.dept, 
            self.email_id, self.designation, self.photo,
            self.bio, self.publications, self.qualification, self.honours_and_awards, self.contact, self.interests)#, self.subjects_even, self.subjects_odd,
            #self.password)
    def get_id(self):
        return self.faculty_id
    '''
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 

    '''



