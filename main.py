# -*- coding: utf-8 -*-
from flask import Flask, render_template, Markup
from flask_assets import Environment
#from flask_debugtoolbar import DebugToolbarExtension
from models import *
import json


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
from assets import bundles
db.init_app(app)
#toolbar = DebugToolbarExtension(app)

assets = Environment(app)
assets.register(bundles)


@app.route('/')
def index():
    arcList = Events.query.order_by(Events.date.desc()).limit(4)
    arcList1 = News.query.order_by(News.news_id.desc()).limit(8)
    return render_template('index_new.html', event_list= arcList, news_lists= arcList1)

# @app.route('/index2/')
# def index2():
#     """Return a friendly HTTP greeting."""
#     return render_template('index2.html')

# @app.route('/index_new/')
# def index_new():
#     """Return a friendly HTTP greeting."""
#     return render_template('index.html')

# @app.route('/index_blue/')
# def index_blue():
#     """Return a friendly HTTP greeting."""
#     return render_template('index_blue.html')

# @app.route('/index_fiu/')
# def index_fiu():
#     """Return a friendly HTTP greeting."""
#     return render_template('index_fiu.html')

# @app.route('/index_red/')
# def index_red():
#     """Return a friendly HTTP greeting."""
#     return render_template('index_red.html')

#################### TEST ###################################
@app.route('/news/')
def news():
    arcList = News.query.order_by(News.news_id.desc()).limit(10)
    return render_template('news.html', news_lists = arcList)

###################### Alumni Routes ##########################
# @app.route('/alumni/')
# def alumni_main():
#     return render_template('alumni.html')

@app.route('/alumni/')
def alumni():
    return render_template('alumni.html')

@app.route('/esteemed-alumni/')
def esteemed_alumni():
    return render_template('esteemed_alumni.html')


####################### LIFE AT NSIT ##################### 
@app.route('/campus-life/')
def campus_life():
    # return render_template('campus_life.html')
    return render_template('hostels.html')

@app.route('/campus-life/housing/')
def campus_life_housing():
    return render_template('housing.html')

@app.route('/campus-life/hostels/')
def campus_life_hostels():
    return render_template('hostels.html')

@app.route('/student-facilities/canteens/')
def campus_life_canteens():
    return render_template('canteens.html')

@app.route('/student-facilities/shopping/')
def student_facilities_shopping():
    return render_template('shopping.html')

@app.route('/student-facilities/medical_help/')
def campus_life_medical_help():
    return render_template('medical_help.html')

@app.route('/student-facilities/sports/')
def sports():
    return render_template('sports.html')

@app.route('/student-facilities/bank/')
def bank():
    return render_template('bank.html')

@app.route('/student-activities/societies/')
def societies():
    return render_template('societies.html')

@app.route('/student-activities/festivals/')
def festivals():
    return render_template('festivals.html')

@app.route('/Statutory-Information/Extension-of-Approval/')   
def extension_approval():
    return render_template('extension_approval.html')

@app.route('/Statutory-Information/BOGMinutes/') 	
def bog_minutes():	
    notices = Notices.query.filter_by(category=7).order_by(Notices.notice_id.desc())
    # GET notices from db
    return render_template('BOGMinutes.html', notices = notices)
	
@app.route('/Statutory-Information/RecruitmentRules/') 	
def recruitment_rules():	
    notices = Notices.query.filter_by(category=8).order_by(Notices.notice_id.desc())
    # GET notices from db
    return render_template('NSITRecruitmentRules.html', notices = notices)

@app.route('/student-activities/student-affairs-council/')
def student_affairs_council():
    return render_template('student_affairs_council.html')


####################### FACULTY ##################### 
# @app.route('/faculty/')
# def faculty():
#     return render_template('faculty.html')

@app.route('/faculty/<fid>/')
def faculty_profile(fid):
    fac = Faculty.query.filter_by(faculty_id=fid).first()
    if fac:
        fac.bio = Markup(fac.bio)
        fac.publications = Markup(fac.publications)
        fac.interests = Markup(fac.interests)
        fac.honours_and_awards = Markup(fac.honours_and_awards)
        if fac.dept == 'COE':
            fac.dept = 'Computer Engineering'
        elif fac.dept == 'ECE':
            fac.dept = 'Electronics and Communications Engineering'
        elif fac.dept == 'ICE':
            fac.dept = 'Instrumentation and Control Engineering'
        elif fac.dept == 'MPAE':
            fac.dept = 'Manufacturing Processes and Automation Engineering'
        elif fac.dept == 'IT':
            fac.dept = 'Information Technology'
        elif fac.dept == 'BT':
            fac.dept = 'Biotechnology'
        elif fac.dept == 'MTH':
            fac.dept = 'Mathematics'
        elif fac.dept == 'CHEM':
            fac.dept = 'Chemistry'
        elif fac.dept == 'PHY':
            fac.dept = 'Physics'
        elif fac.dept == 'HSS':
            fac.dept = 'Humanities and Social Sciences'
        elif fac.dept == 'MG':
            fac.dept = 'Management'

        ### logic for page editing ###
        return render_template('faculty_profile.html',faculty = fac)
        
    return "NOT FOUND" #MAKE PAGE

######################### DIRECTOR #############################
@app.route('/director/')
def director():
    return render_template('director.html')

@app.route('/chairman/')
def chairman():
    return render_template('chairman.html')

@app.route('/registrar/')
def registrar():
    return render_template('registrar.html')

@app.route('/list-of-directors/')
def list_of_directors():
    with open(str('data/directors/directorList.json')) as f:
        direcList_data = json.load(f)
    for director in direcList_data['directors']:
        director['name'] = Markup(director['name'])
        director['desig'] = Markup(director['desig'])
        director['start'] = Markup(director['start'])
        director['end'] = Markup(director['end'])
    return render_template('list_of_directors.html', direcList_data=direcList_data['directors'])

@app.route('/list-of-chairmen/')
def list_of_chairmen():
    with open(str('data/chairmen/chairList.json'),encoding='utf8') as f:
        chairList_data = json.load(f)
    for chairman in chairList_data['chairmen']:
        chairman['name'] = Markup(chairman['name'])
        chairman['desig'] = Markup(chairman['desig'])
    return render_template('list_of_chairmen.html', chairList_data=chairList_data['chairmen'])

@app.route('/president/')
def president():
    return render_template('president_nsit.html')

####################### STUDENT ACTIVITIES #####################
#@app.route('/student_activities/')
#def student_activites_main():
#    return render_template('student_activities.html')

@app.route('/placement/')
def placement():
    return render_template('placement.html')

####################### SOCIAL INITIATIVES ##############################
# @app.route('/social_initiatives/')
# def social_initiatives_main():
#     return render_template('social_initiatives.html')

####################### FACILITIES ROUTES ######################
# @app.route('/facilities/')
# def facilities_main():
#     return render_template('facilities.html')


################### anti-harassment policy #####################
# @app.route('/policy/')
# def policy():
#     return render_template('policy.html')

###################### RTI #####################################
@app.route('/rti/')
def rti():
    return render_template('rti.html')

###################### TENDERS #################################
@app.route('/tenders/')
def tenders():
    tenders = Tenders.query.order_by(Tenders.tender_id.desc())
    # GET tenders from db
    return render_template('tenders.html', tenders = tenders)
    # return render_template('tenders.html')

@app.route('/notices/')
def notices():
    notices = Notices.query.order_by(Notices.notice_id.desc())
    # GET notices from db
    return render_template('notices.html', notices = notices)

@app.route('/recruitment/')
def recruitment():
    return render_template('recruitment.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     """Return a custom 404 error."""
#     return 'Sorry, Nothing at this URL.', 404


# @app.errorhandler(500)
# def page_not_found(e):
#     """Return a custom 500 error."""
#     return 'Sorry, unexpected error: {}'.format(e), 500

###################### About #################################

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/about/vision/')
def about_vision():
    return render_template('vision.html')

@app.route('/about/history/')
def about_history():
    return render_template('history.html')

@app.route('/administration/')
def administration():
    return render_template('administration.html')

@app.route('/admissions/contact/')
def admissions():
    return render_template('admissions.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/library/')
def library():
    return render_template('library.html')

@app.route('/sandt/')
def sandt():
    return render_template('sandt.html')

@app.route('/location/')
def location():
    return render_template('location.html')

# @app.route('/conference/')
# def conference():
#     return render_template('conference.html')

#@app.route('/academics/')
#def academics():
#    return render_template('academics.html')

###################### About #################################

@app.route('/academics/courses/')
def academics():
    return render_template('courses.html')

@app.route('/academics/academic_system/')
def academic_system():
    return render_template('academic_system.html')

@app.route('/academics/curriculum/')
def curriculum():
    return render_template('curriculum.html')

@app.route('/academics/academic-calender/')
def academic_calender():
    return render_template('academic_calender.html')

@app.route('/academics/fee-structure/')
def fee_structure():
    return render_template('fee_structure.html')

@app.route('/divisions/')
def department():
    return render_template('department.html')

@app.route('/division/<deptname>/')
def dept_geninfo(deptname):
    with open(str('data/dept_geninfo/'+deptname+'.json')) as f:
        dept_data = json.load(f)
    dept_data['info'] = Markup(dept_data['info'])
    return render_template('dept_gen_info.html', dept_data = dept_data, dept_code = deptname)

@app.route('/division/<deptname>/labs/')
def dept_labs(deptname):
    try:
        with open('data/dept_labs/'+deptname+'.json') as f:
            dept_data = json.load(f)
        for lab in dept_data['labs']:
            lab['info'] = Markup(lab['info'])
        return render_template('dept_labs.html', deptname = dept_data['name'], data = dept_data)
    except:
        return render_template('under_construction.html')

@app.route('/division/<deptname>/faculty/')
def dept_faculty(deptname):
    with open(str('data/dept_geninfo/'+deptname+'.json')) as f:
        dept_data = json.load(f)
    dept_data['info'] = Markup(dept_data['info'])
    fac = Faculty.query.filter_by(dept=deptname).order_by('rank').all()
    # for f in fac:
    #     print f.name
    return render_template('dept_faculty.html', dept=deptname,fac=fac, dept_data=dept_data)

@app.route('/division/<deptname>/scholars/')
def dept_scholars(deptname):
    ###SCHOLARS###
    with open(str('data/dept_geninfo/'+deptname+'.json')) as f:
        dept_data = json.load(f)
    name = dept_data['name']
    stu = Student.query.filter_by(dept=deptname.upper()).all()
    fac = []
    for s in stu:
        if s.guide != None:
            try:
                f = Faculty.query.filter_by(faculty_id=s.guide).first()
                fac.append(f.title + ' ' + f.name)
            except:
                fac.append(None)
        else:
            fac.append(None)
    return render_template('dept_scholars.html', deptname = name, stu = list(zip(stu, fac)))

@app.route('/division/<deptname>/staff/')
def dept_staff(deptname):
    ###STAFF###
    with open(str('data/dept_geninfo/'+deptname+'.json')) as f:
        dept_data = json.load(f)
    name = dept_data['name']


    try:
        with open(str('data/staff/'+deptname+'.json')) as f:
            data = json.load(f)
        staff_name = []
        staff_des = []
        room = []
        for i in data:
            staff_name.append(i['name'])
            staff_des.append(i['des'])
            if i['room'] != "" :
                room.append(i['room'])
    
        if not room:
            flag = 0
        else:
            flag = 1
    
    except:
        staff_name = []
        staff_des = []
        room = []
        flag = 0

    #return 'hello'    
    return render_template('dept_staff.html', deptname=name, staff = list(zip(staff_name,staff_des,room)) , flag = flag)



#@app.route('/division/coe/')
#def dept_coe():
#    fac = Faculty.query.filter_by(dept='COE').all()
#    return render_template('coe_gen_info.html', fac = fac)

# @app.route('/division/coe2/')
# def dept_coe2():
#     fac = Faculty.query.filter_by(dept='COE').all()
#     return render_template('coe.html', fac = fac)

#@app.route('/division/ece/')
#def dept_ece():
#    fac = Faculty.query.filter_by(dept='ECE').all()
#    return render_template('ece.html', fac = fac)

#@app.route('/division/ice/')
#def dept_ice():
#    fac = Faculty.query.filter_by(dept='ICE').all()
#    return render_template('ice.html', fac = fac)

#@app.route('/division/ice/labs/')
#def dept_ice_labs():
#    return render_template('ice_labs.html')

#@app.route('/division/mpae/')
#def dept_mpae():
#    fac = Faculty.query.filter_by(dept='MPAE').all()
#    return render_template('mpae.html', fac = fac)

#@app.route('/division/mpae/labs/')
#def dept_mpae_labs():
#    return render_template('mpae_labs.html')

#@app.route('/division/it/')
#def dept_it():
#    fac = Faculty.query.filter_by(dept='IT').all() #returns a list
#    #print fac[0].name
#    return render_template('it.html', fac = fac)

#@app.route('/division/bt/')
#def dept_bt():
#    fac = Faculty.query.filter_by(dept='BT').all() #returns a list
#    # print fac[0].name
#    return render_template('bt.html', fac = fac)

#@app.route('/division/phy/')
#def dept_phy():
#    fac = Faculty.query.filter_by(dept='PHY').all() #returns a list
#    #print fac[0].name
#    return render_template('phy.html', fac = fac)

#@app.route('/division/mth/')
#def dept_mth():
#    fac = Faculty.query.filter_by(dept='MTH').all() #returns a list
#    #print fac[0].name
#    return render_template('mth.html', fac = fac)

#@app.route('/division/chm/')
#def dept_chm():
#    fac = Faculty.query.filter_by(dept='CHEM').all() #returns a list
#    #print fac[0].name
#    return render_template('chem.html', fac = fac)

#@app.route('/division/mg/')
#def dept_mg():
#    fac = Faculty.query.filter_by(dept='MG').all() #returns a list
#    #print fac[0].name
#    return render_template('mg.html', fac = fac)

#@app.route('/division/hss/')
#def dept_hss():
#    fac = Faculty.query.filter_by(dept='HSS').all() #returns a list
#    #print fac[0].name
#    return render_template('hss.html', fac = fac)

@app.route('/research/')
def research():
    # return render_template("research.html")
    return render_template("under_construction.html")

@app.route('/disclaimer/')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/achievements/')
def achievements():
    return render_template('achievements.html')

@app.route('/media/')
def media():
    return render_template('media.html')

@app.route('/media/videos/')
def media_videos():
    return render_template('video_gallery.html')

@app.route('/under_construction/')
def under_construction():
    return render_template('under_construction.html')

@app.route('/web-team/')
def web_team():
    return render_template('web_team.html')

@app.route('/board-of-governers/')
def bog():
    with open(str('data/gcBog/bog.json')) as f:
        bog_data = json.load(f)
    for bog in bog_data['bog']:
        bog['name'] = Markup(bog['name'])
        bog['desc'] = Markup(bog['desc'])
        if 'info' in bog:
            bog['info'] = Markup(bog['info'])
    return render_template('bog.html', bog_data=bog_data['bog'])

@app.route('/examination/')
def examination():
    # return render_template("results.html")
    return render_template("examination.html")

@app.route('/general-council/')
def gc():
    with open(str('data/gcBog/gc.json')) as f:
        gc_data = json.load(f)
    for gc in gc_data['gc']:
        gc['name'] = Markup(gc['name'])
        gc['desc'] = Markup(gc['desc'])
    return render_template('gc.html', gc_data=gc_data['gc'])

@app.route('/download-forms/')
def download_forms():
    return render_template('internal_forms.html')

#@app.route('/division/coe/labs/')
#def dept_coe_labs():
#    return render_template('coe_labs.html')

#@app.route('/division/bt/labs/')
#def bt_labs():
#    return render_template('bt_labs.html')



#@app.route('/division/ece/labs/')
#def ece_labs():
 #   return render_template('ece_labs.html')




#@app.route('/division/chm/labs/')
#def chm_labs():
#    return render_template('chm_labs.html')

@app.route('/article/<article_id>/')
def article(article_id):
    arc = News.query.filter_by(news_id=article_id).first()
    # print arc
    arc.text = Markup((arc.text))
    arcList = News.query.order_by(-News.news_id.desc()).limit(5)
    # print arcList
    if arc.photo == None:
        arc.photo = 'None'
    return render_template('article_new.html', article = arc)

@app.route('/events/open-day/')
def events_open_day():
    return render_template('events_open_day.html')

@app.route('/results/')
def results():
    return render_template('results.html')

@app.route('/photo-gallery/')
def photo_gallery():
    return render_template('photo_gallery.html')

@app.route('/why-nsit/')
def why_nsit():
    return render_template('why_nsit.html')

@app.route('/about-campus/')
def about_campus():
    return render_template('about_campus.html')

@app.route('/campus-life/blocks/')
def campus_life_blocks():
    return render_template('blocks.html')

@app.route('/student-facilities/')
def student_facilities():
    return render_template('student_facilities.html')

@app.route('/student-facilities/societies/technical/')
def technical_societies():
    return render_template('technical_societies.html')

@app.route('/student-facilities/societies/non_technical/')
def non_technical_societies():
    return render_template('non_technical_societies .html')

@app.route('/student-facilities/societies/automotive/')
def automotive_clubs():
    return render_template('automotive_clubs.html')


@app.route('/student-facilities/societies/literary/')
def literary_clubs():
    return render_template('literary_clubs.html')


@app.route('/student-facilities/societies/recreational/')
def recreational_clubs():
    return render_template('recreational_clubs.html')

@app.route('/student-facilities/societies/community-service-initiatives/')
def comm_service_initiatives():
    return render_template('comm_service_initiatives.html')

@app.route('/list-of-deans/')
def list_of_deans():
    with open(str('data/deans/deanList.json')) as f:
        deanList_data = json.load(f)
    for dean in deanList_data['deans']:
        dean['name'] = dean['name']
        dean['desig'] = dean['desig']
    return render_template('list_of_deans.html', deanList_data=deanList_data['deans'])
    # return render_template('under_construction.html')

'''
@app.route('/mpae_fac')
def mpae_fac():
    fac = Faculty.query.filter_by(dept='MPAE').all()
    return render_template('department_fac.html', fac = fac)

@app.route('/mpae_about')
def mpae_about():
    return render_template('aboutmpae.html')

@app.route('/mpae_cur')
def mpae_cur():
       return render_template('curmpae.html')

@app.route('/mpae_stu')
def mpae_stu():
       return render_template('stumpae.html')


@app.route('/mpae_staff')
def mpae_staff():
       return render_template('staffmpae.html')


@app.route('/mpae_res')
def mpae_res():
       return render_template('resmpae.html')
	   @app.route('/student-facilities/societies/community-service-initiatives/')
'''




if __name__ == '__main__':
    db.app = app
    db.create_all()
    app.run()
