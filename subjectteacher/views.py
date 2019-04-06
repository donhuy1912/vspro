from django.shortcuts import render, redirect
from userdetail.models import *
from datetime import datetime

# Create your views here.

def index(request):
    subjectteachers = SubjectTeacher.objects.all()
   
    for subjectteacher in subjectteachers:
        subjectteacher.createdate = subjectteacher.createdate
        subjectteacher.editdate = subjectteacher.editdate

    context = {'subjectteachers': subjectteachers}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        subjectteacher = SubjectTeacher( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectid = Subject.objects.get(subjectid = request.POST['subjectid']),
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        subjectteacher.save()
        return redirect('/tables_object/')
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
            'accounts':accounts,
            'subjects':subjects,
        }
    return render(request, 'subjectteacher/subjectteacher_create.html', context)

def edit(request, id):
    subjectteacher = SubjectTeacher.objects.get(subjectteacherid=id)
    subjectteacher.createdate = subjectteacher.createdate
    subjectteacher.editdate = datetime.now()

    accounts = Account.objects.all()
    subjects = Subject.objects.all()
    
    for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate
        
    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate

    context = {
        'subjectteacher': subjectteacher,
        'accounts':accounts,
        'subjects':subjects,
    }
    return render(request, 'subjectteacher/subjectteacher_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    subjectteacher = SubjectTeacher.objects.filter(subjectteacherid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    subjectteacher = SubjectTeacher.objects.filter(subjectteacherid = id).update(subjectid = Subject.objects.get(subjectid = getNum(request.POST['subjectid'])))
    subjectteacher = SubjectTeacher.objects.get(subjectteacherid=id)
    subjectteacher.createdate = subjectteacher.createdate
    subjectteacher.editdate = datetime.now()
    subjectteacher.isenable = request.POST['isenable']
    subjectteacher.note = request.POST['note']
    subjectteacher.save()
    return redirect('/tables_object/')


def delete(request, id):
    subjectteacher = SubjectTeacher.objects.get(subjectteacherid= id)
    subjectteacher.delete()
    return redirect('/tables_object/')