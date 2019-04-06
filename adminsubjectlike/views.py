from django.shortcuts import render, redirect
from homepage.models import SubjectLike, Subject, Account, Subject
from datetime import datetime

# Create your views here.

def index(request):
    subjectlikes = SubjectLike.objects.all()
    # for subjectlike in subjectlikes:
    #     subjectlike.createdate = subjectlike.createdate
    #     subjectlike.editdate = subjectlike.editdate
    context = {'subjectlikes': subjectlikes }
    return render(request, 'adminsubjectlike/subjectlike_show.html', context)

def create(request):
    if request.method == 'POST':
        subjectlike = SubjectLike( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectid = Subject.objects.get(subjectid = request.POST['subjectid']),
                                status=request.POST['status'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        subjectlike.save()
        return redirect('/adminsubjectlike/')
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
    return render(request, 'adminsubjectlike/subjectlike_create.html', context)

def edit(request, id):
    subjectlike = SubjectLike.objects.get(subjectlikeid=id)
    
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
        'subjectlike': subjectlike
    }

    return render(request, 'adminsubjectlike/subjectlike_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    subjectlike = SubjectLike.objects.filter(subjectlikeid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    subjectlike = SubjectLike.objects.filter(subjectlikeid = id).update(subjectid = Subject.objects.get(subjectid = getNum(request.POST['subjectid'])))
    subjectlike = SubjectLike.objects.get(subjectlikeid=id)
    subjectlike.status=request.POST['status']
    subjectlike.isenable=request.POST['isenable']
    subjectlike.note=request.POST['note']
    subjectlike.save()
    return redirect('/adminsubjectlike/')


def delete(request, id):
    subjectlike = SubjectLike.objects.get(subjectlikeid= id)
    subjectlike.delete()
    return redirect('/adminsubjectlike/')