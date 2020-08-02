from . import db

class Tenders(db.Model):
	__tablename__ = 'tenders'
	tender_id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
	title = db.Column(db.String(100))
	new = db.Column(db.Integer())
	date_of_release = db.Column(db.String(30))
	due_date = db.Column(db.String(30))
	url = db.Column(db.String(500))

#support constructor with no arguments so that rows can be added from admin panel
	def __init__(self, title="", new = 0, date_of_release="", due_date="", url=""):
		self.title = title
		self.new = new
		self.date_of_release = date_of_release
		self.due_date = due_date
		self.url = url

	def __repr__(self):
		return "<Tenders(tender_id='%s',title='%s',new='%s',date_of_release='%s',due_date='%s',url='%s')>" % (
			self.tender_id, self.title, self.new, self.date_of_release, self.due_date, self.url)

	def get_id(self):
		return self.faculty_id