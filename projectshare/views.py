from django.shortcuts import render, redirect
from userdetail.models import ProjectShare, SubjectPart, Account, Subject
from datetime import datetime
from homepage.myfunction import tokenFile
from django.http import JsonResponse

# Create your views here.

def index(request):
    projectshares = ProjectShare.objects.all()
    for projectshare in projectshares:
        projectshare.createdate = projectshare.createdate
        projectshare.editdate = projectshare.editdate
    context = {'projectshares': projectshares}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        if(request.POST.get('subjectpartid')=='0'):
            subjectpartid = None
        else:
            subjectpartid = SubjectPart.objects.get(subjectpartid = request.POST['subjectpartid'])
        try:
            token_link = request.FILES['link']
        except:
            token_link = None
        lin = ''
        if token_link != None:
            lin = tokenFile(token_link)
        projectshare = ProjectShare( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectpartid = subjectpartid,
                                projectsharetopicname=request.POST['projectsharename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=lin,
                                viewcount=request.POST['viewcount'],  
                                likecount=request.POST['likecount'],  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        projectshare.save()
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
       
    return render(request, 'projectshare/projectshare_create.html', context)

def edit(request, id):
    projectshare = ProjectShare.objects.get(projectsharetopicid=id)
    projectshare.createdate = projectshare.createdate
    projectshare.editdate = datetime.now()

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
        'projectshare': projectshare,
        'subjectparts': subjectparts
    }
    
    return render(request, 'projectshare/projectshare_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    
    projectshare = ProjectShare.objects.filter(projectsharetopicid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    if request.POST.get('subjectpartid')!= '0':
        projectshare = ProjectShare.objects.filter(projectsharetopicid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    projectshare = ProjectShare.objects.get(projectsharetopicid=id)
    if request.POST.get('subjectpartid')  == '0':
        projectshare.subjectpartid=None
    # projectshare = ProjectShare.objects.filter(projectsharetopicid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    projectshare = ProjectShare.objects.get(projectsharetopicid=id)
    projectshare.projectsharetopicname=request.POST['projectsharename']
    projectshare.createdate=projectshare.createdate
    projectshare.editdate=datetime.now()
    projectshare.content=request.POST['content']
    projectshare.link=request.POST['link']
    projectshare.viewcount=request.POST['viewcount']
    projectshare.likecount=request.POST['likecount']
    projectshare.isenable=request.POST['isenable']
    projectshare.note=request.POST['note']
    projectshare.save()
    return redirect('/tables_object/')


def delete(request, id):
    projectshare = ProjectShare.objects.get(projectsharetopicid= id)
    projectshare.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
def validate_subjectprojectshare(request):
    subject = request.GET.get('subject', None)
    s = ''

    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        projectshare  = ProjectShare.objects.get(projectsharetopicid = request.GET.get('projectshare', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
        if(subject == "0"):
            s = '<option type="text" name="subjectpartid" value="0">Chung</option>'
    else:
        if change == False:
            if projectshare.subjectpartid != None:
                s= ' <option type="text" name="subjectpartid" value="' + str(projectshare.subjectpartid.subjectpartid) + ' ">' + projectshare.subjectpartid.subjectpartname + '</option>'
            else:
                s= '<option type="text" name="subjectpartid" value="0">Chung</option>'
    
    temp = ''
    
    if subject == None:
        subjectparts = None
    else:
        subjectparts = SubjectPart.objects.filter(subjectid=subject)
        for subjectpart in subjectparts: 
            if edit == True and change == False:
                if subjectpart.subjectpartid != projectshare.subjectpartid.subjectpartid:
                        temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
            else:
                temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
            s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)