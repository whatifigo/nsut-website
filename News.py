from . import db
from datetime import datetime


class News(db.Model):
    __tablename__ = 'news'
    news_id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(500))
    author = db.Column(db.String(50))
    date = db.Column(db.DateTime(70), onupdate = datetime.now())
    email_id = db.Column(db.String(100))
    photo = db.Column(db.String(500))
    caption = db.Column(db.String(10000))
    text = db.Column(db.Text())
    url = db.Column(db.String(500))
    '''
    subjects_odd = db.Column(db.String(2000))
    subjects_even = db.Column(db.String(2000))
    password = db.Column(db.String(50))
    '''

    #support constructor with no arguments so that rows can be added from admin panel
    def __init__(self, title="", author="", dept="",
                email_id="", photo="",  subtitle="", 
                caption ="" ,text = "", url=""):#, subjects_odd="",
                #subjects_even="", password=""):
        self.title = title
        self.author = author
        self.subtitle = subtitle
        self.email_id = email_id
        self.caption = caption
        self.photo = photo
        self.text = text
        self.url = url
        '''
        self.subjects_odd = subjects_odd
        self.subjects_even = subjects_even
        self.password = md5(str(password)).hexdigest()
        '''
    def __repr__(self):
        return "<News(news_id='%s',title='%s' ,author='%s', subtitle='%s', email_id='%s', caption='%s', photo='%s', text='%s', date='%s')>" % (
            self.news_id, self.title, self.author, self.subtitle, 
            self.email_id, self.caption, self.photo,
            self.text, self.date)#, self.subjects_even, self.subjects_odd,
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