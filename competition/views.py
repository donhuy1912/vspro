from django.shortcuts import render, redirect
from userdetail.models import Competition, SubjectPart, Account, Subject
from datetime import datetime
from django.http import JsonResponse

# Create your views here.

def index(request):
    competitions = Competition.objects.all()
    for competition in competitions:
        competition.createdate = competition.createdate
        competition.editdate = competition.editdate
        competition.opendate = competition.opendate.strftime("%Y-%m-%d %H:%M:%S")
        competition.enddate = competition.enddate.strftime("%Y-%m-%d %H:%M:%S")
    context = {'competitions': competitions}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        if(request.POST.get('subjectpartid')=='0'):
            subjectpartid = None
        else:
            subjectpartid = SubjectPart.objects.get(subjectpartid = request.POST['subjectpartid'])
        competition = Competition( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectpartid = subjectpartid,
                                competitionname=request.POST['competitionname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                opendate= request.POST['opendate'],
                                enddate= request.POST['closedate'],
                                content=request.POST['content'],
                                viewcount=request.POST['viewcount'],  
                                likecount=request.POST['likecount'],  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        competition.save()
        return redirect('/tables_object/')
    else:
        subjectparts = SubjectPart.objects.all()
        for subjectpart in subjectparts:
            subjectpart.createdate = subjectpart.createdate
            subjectpart.editdate = subjectpart.editdate
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
            'subjectparts': subjectparts
        }
       
    return render(request, 'competition/competition_create.html', context)

def edit(request, id):
    competition = Competition.objects.get(competitionid=id)
    competition.createdate = competition.createdate
    competition.editdate = datetime.now()
    competition.opendate = competition.opendate.strftime("%Y-%m-%d %H:%M:%S")
    competition.enddate = competition.enddate.strftime("%Y-%m-%d %H:%M:%S")

    subjectparts = SubjectPart.objects.all()
    for subjectpart in subjectparts:
        subjectpart.createdate = subjectpart.createdate
        subjectpart.editdate = subjectpart.editdate

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
        'competition': competition,
        'subjectparts': subjectparts
    }

    return render(request, 'competition/competition_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    competition = Competition.objects.filter(competitionid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    if request.POST.get('subjectpartid')!= '0':
        competition = Competition.objects.filter(competitionid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    competition = Competition.objects.get(competitionid=id)
    print(request.POST.get('subjectpartid')==0)
    if request.POST.get('subjectpartid')  == '0':
        competition.subjectpartid=None
    # competition = Competition.objects.filter(competitionid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    competition = Competition.objects.get(competitionid=id)
    competition.competitionname=request.POST['competitionname']
    competition.createdate=competition.createdate
    competition.editdate=datetime.now()
    competition.opendate= request.POST['opendate']
    competition.enddate= request.POST['closedate']
    competition.content=request.POST['content']
    competition.viewcount=request.POST['viewcount']
    competition.likecount=request.POST['likecount']
    competition.isenable=request.POST['isenable']
    competition.note=request.POST['note']
    competition.save()
    return redirect('/tables_object/')


def delete(request, id):
    competition = Competition.objects.get(competitionid= id)
    competition.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
def validate_subjectcompetition(request):
    subject = request.GET.get('subject', None)
    subjectparts = SubjectPart.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        competition  = Competition.objects.get(competitionid = request.GET.get('competition', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
        if(subject == "0"):
            s = '<option type="text" name="subjectpartid" value="0">Chung</option>'
    else:
        if change == False:
            if competition.subjectpartid != None:
                s= ' <option type="text" name="subjectpartid" value="' + str(competition.subjectpartid.subjectpartid) + ' ">' + competition.subjectpartid.subjectpartname + '</option>'
            else:
                s= '<option type="text" name="subjectpartid" value="0">Chung</option>'
    temp = ''

    for subjectpart in subjectparts: 
        if edit == True and change == False:
            if subjectpart.subjectpartid != competition.subjectpartid.subjectpartid:
                    temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        else:
            temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)