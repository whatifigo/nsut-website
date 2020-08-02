from flask import Flask
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
from models import *

import os.path as op
path = op.join(op.dirname(__file__), 'static')

adminapp = Flask(__name__, instance_relative_config=True)

adminapp.config.from_pyfile('config.py') #instance folder
#adminapp.config.from_envvar('APP_CONFIG_FILE') #config file for server

admin = Admin(name = "NSIT")
admin.init_app(adminapp)

db.init_app(adminapp)

##### VIEWS #####
class PageView(BaseView):
    def is_accessible(self):
        return True
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

##### DB ADMIN #####
class FacultyView(ModelView):
    create_template = 'admin/tinymce.html'
    edit_template = 'admin/tinymce.html'
    can_create = True
    can_edit = True
    column_display_pk = True #display primary key
    #rename column for display
    column_labels = dict(aoi='Areas of interest')
    
    form_columns = ('faculty_id', 'title', 'name', 'dept', 
            'email_id', 'designation','photo','bio', 'publications', 'qualification','honours_and_awards',
            'contact','interests','rank')
    column_list = ('faculty_id', 'title', 'name', 'dept', 
                'email_id', 'designation', 'qualification',
                'contact','photo','rank'
                )

    column_filters = ('faculty_id', 'name', 'dept')
    
    def __init__(self, session, **kwargs):
        super(FacultyView, self).__init__(Faculty, session, **kwargs)

admin.add_view(FacultyView(db.session, category='DataBase'))

class StudentView(ModelView):
    can_create = True
    can_edit = True
    column_display_pk = True #display primary key
    column_filters = ('name', 'dept', 'guide')
    
    def __init__(self, session, **kwargs):
        super(StudentView, self).__init__(Student, session, **kwargs)

admin.add_view(StudentView(db.session, category='DataBase'))


class NewsView(ModelView):
    can_create = True
    can_edit = True
    column_display_pk = True #display primary key
    column_filters = ('title', 'subtitle', 'author', 'email_id', 'photo',  'caption', 'text', 'url')
    
    def __init__(self, session, **kwargs):
        super(NewsView, self).__init__(News, session, **kwargs)

admin.add_view(NewsView(db.session, category='DataBase'))

class NoticesView(ModelView):
    can_create = True
    can_edit = True
    column_display_pk = True #display primary key
    column_filters = ('title', 'category', 'new', 'url')
    
    def __init__(self, session, **kwargs):
        super(NoticesView, self).__init__(Notices, session, **kwargs)

admin.add_view(NoticesView(db.session, category='DataBase'))

class TendersView(ModelView):
    can_create = True
    can_edit = True
    column_display_pk = True
    column_filters = ('title', 'new', 'date_of_release', 'due_date', 'url')
    def __init__(self, session, **kwargs):
        super(TendersView, self).__init__(Tenders, session, **kwargs)

admin.add_view(TendersView(db.session, category='DataBase'))        

class EventsView(ModelView):
    can_create = True
    can_edit = True
    column_display_pk = True #display primary key
    column_filters = ('title', 'date','duration','venue','description','url')
    
    def __init__(self, session, **kwargs):
        super(EventsView, self).__init__(Events, session, **kwargs)

admin.add_view(EventsView(db.session, category='DataBase'))

##### FILE ADMIN #####
class ImageAdmin(FileAdmin):
    can_rename = False #disallow rename
    allowed_extensions = ('jpeg', 'jpg', 'gif', 'png', 'bmp')

class CSSAdmin(FileAdmin):
    allowed_extensions = ('css')

admin.add_view(ImageAdmin(path+'/images/', name='Images', category='Files'))
admin.add_view(CSSAdmin(path+'/css/', name='CSS', category='Files'))

@adminapp.route('/')
def index():
    return "<a href ='/admin'>Use /admin</a>"

if __name__ == "__main__":
    db.app = adminapp
    db.create_all()
    adminapp.run(host = "127.0.0.1",port = 8001)