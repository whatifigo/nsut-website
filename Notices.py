from . import db

class Notices(db.Model):
	__tablename__ = 'notices'
	notice_id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
	title = db.Column(db.String(100))
	category = db.Column(db.Integer())
	new = db.Column(db.Integer())
	url = db.Column(db.String(500))

#support constructor with no arguments so that rows can be added from admin panel
	def __init__(self, title="", category = 0, new = 0, url=""):
		self.title = title
		self.category = category
		self.new = new
		self.url = url

	def __repr__(self):
		return "<Notice(news_id='%s',title='%s')>" % (
			self.notice_id, self.title)

	def get_id(self):
		return self.faculty_id