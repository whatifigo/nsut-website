from . import db
from datetime import datetime

class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime())
    duration = db.Column(db.String(100))
    venue = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
   
    #support constructor with no arguments so that rows can be added from admin panel
    def __init__(self, event_id="", title="", date="", duration="",venue="", description="", url=""):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.duration = duration
        self.venue = venue
        self.description = description
        self.url = url

    def __repr__(self):
        return "<Events(event_id='%s',title='%s' ,date='%s',duration='%s',venue='%s',description='%s', url='%s')>" % (
            self.event_id, self.title, self.date, self.duration, self.venue, self.description, self.url)

    def get_id(self):
        return self.event_id