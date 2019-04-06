from django.shortcuts import render, redirect
from userdetail.models import *
from datetime import datetime
# Create your views here.

def index(request):
    enrollments = Enrollment.objects.all()
    subjectlikes = SubjectLike.objects.all()
    lessonreplys = LessonReply.objects.all()
    activityreplys = ActivityReply.objects.all()
    activitysubmittionreplys = ActivitySubmittionReply.objects.all()
    trackings = Tracking.objects.all()
    forumlikes = ForumLike.objects.all()
    forumreplys = ForumReply.objects.all()
    newsreplys = NewsReply.objects.all()
    projectsharereplys = ProjectShareReply.objects.all()
    projectsharelikes = ProjectShareLike.objects.all()
    competitionsubmittionlikes = CompetitionSubmittionLike.objects.all()
    competitionsubmittionreplys = CompetitionSubmittionReply.objects.all()

    for enrollment in enrollments:
        enrollment.createdate = enrollment.createdate
        enrollment.editdate = enrollment.editdate

    for lessonreply in lessonreplys:
        lessonreply.createdate = lessonreply.createdate
        lessonreply.editdate = lessonreply.editdate

    for activityreply in activityreplys:
        activityreply.createdate = activityreply.createdate
        activityreply.editdate = activityreply.editdate

    for activitysubmittionreply in activitysubmittionreplys:
        activitysubmittionreply.createdate = activitysubmittionreply.createdate
        activitysubmittionreply.editdate = activitysubmittionreply.editdate

    for tracking in trackings:
        tracking.createdate = tracking.createdate
        tracking.editdate = tracking.editdate

    for forumreply in forumreplys:
        forumreply.createdate = forumreply.createdate
        forumreply.editdate = forumreply.editdate

    for newsreply in newsreplys:
        newsreply.createdate = newsreply.createdate
        newsreply.editdate = newsreply.editdate

    for projectsharereply in projectsharereplys:
        projectsharereply.createdate = projectsharereply.createdate
        projectsharereply.editdate = projectsharereply.editdate

    for competitionsubmittionreply in competitionsubmittionreplys:
        competitionsubmittionreply.createdate = competitionsubmittionreply.createdate
        competitionsubmittionreply.editdate = competitionsubmittionreply.editdate

    context = {'enrollments': enrollments,
               'subjectlikes': subjectlikes,
               'lessonreplys': lessonreplys,
               'activityreplys': activityreplys,
               'activitysubmittionreplys': activitysubmittionreplys,
               'trackings': trackings,
               'forumlikes': forumlikes,
               'forumreplys': forumreplys,
               'newsreplys': newsreplys,
               'projectsharereplys': projectsharereplys,
               'projectsharelikes': projectsharelikes,
               'competitionsubmittionlikes': competitionsubmittionlikes,
               'competitionsubmittionreplys': competitionsubmittionreplys,
            }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        enrollment = Enrollment( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectid = Subject.objects.get(subjectid = request.POST['subjectid']),
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        enrollment.save()
        return redirect('/tables_relationship/')
    else:
        accounts = Account.objects.all()
        subjects = Subject.objects.all()
        
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate

        for subject in subjects:
            subject.createdate = subject.createdate
            subject.editdate = subject.editdate
        
        context = {
            'accounts': accounts,
            'subjects': subjects,
        }
    return render(request, 'enrollment/enrollment_create.html', context)

def edit(request, id):
    enrollment = Enrollment.objects.get(enrollmentid=id)
    enrollment.createdate = enrollment.createdate
    enrollment.editdate = datetime.now()

    accounts = Account.objects.all()
    subjects = Subject.objects.all()
        
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate
        
    context = {
        'accounts': accounts,
        'subjects': subjects,
        'enrollment': enrollment
    }
    
    return render(request, 'enrollment/enrollment_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    enrollment = Enrollment.objects.filter(enrollmentid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    enrollment = Enrollment.objects.filter(enrollmentid = id).update(subjectid = Subject.objects.get(subjectid = getNum(request.POST['subjectid'])))
    enrollment = Enrollment.objects.get(enrollmentid=id)
    enrollment.createdate = enrollment.createdate
    enrollment.editdate = datetime.now()
    enrollment.isenable = request.POST['isenable']
    enrollment.note = request.POST['note']
    enrollment.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    enrollment = Enrollment.objects.get(enrollmentid= id)
    enrollment.delete()
    return redirect('/tables_relationship/')