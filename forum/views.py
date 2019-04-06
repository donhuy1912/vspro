from django.shortcuts import render, redirect
from userdetail.models import Forum, SubjectPart, Account, Subject
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def index(request):
    forums = Forum.objects.all()
    for forum in forums:
        forum.createdate = forum.createdate
        forum.editdate = forum.editdate
    context = {'forums': forums}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        if(request.POST.get('subjectpartid')=='0'):
            subjectpartid = None
        else:
            subjectpartid = SubjectPart.objects.get(subjectpartid = request.POST['subjectpartid'])
        forum = Forum( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectpartid = subjectpartid,
                                forumtopicname=request.POST['forumname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                viewcount=request.POST['viewcount'],  
                                likecount=request.POST['likecount'],  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        forum.save()
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
            'subjectparts': subjectparts,
        }
       
    return render(request, 'forum/forum_create.html', context)

def edit(request, id):
    forum = Forum.objects.get(forumtopicid=id)
    forum.createdate = forum.createdate
    forum.editdate = datetime.now()

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
        'forum': forum,
        'subjectparts': subjectparts,
        'accounts': accounts,
        'subjects': subjects,
    } 
  
    return render(request, 'forum/forum_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    forum = Forum.objects.filter(forumtopicid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    if request.POST.get('subjectpartid')!= '0':
        forum = Forum.objects.filter(forumtopicid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    forum = Forum.objects.get(forumtopicid=id)
    if request.POST.get('subjectpartid')  == '0':
        forum.subjectpartid=None
    forum.forumtopicname=request.POST['forumname']
    forum.createdate=forum.createdate
    forum.editdate=datetime.now()
    forum.content=request.POST['content']
    forum.viewcount=request.POST['viewcount']
    forum.likecount=request.POST['likecount']
    forum.isenable=request.POST['isenable']
    forum.note=request.POST['note']
    forum.save()
    return redirect('/tables_object/')


def delete(request, id):
    forum = Forum.objects.get(forumtopicid= id)
    forum.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
def validate_subjectforum(request):
    subject = request.GET.get('subject', None)
    subjectparts = SubjectPart.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        forum  = Forum.objects.get(forumtopicid = request.GET.get('forum', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
        if(subject == "0"):
            s = '<option type="text" name="subjectpartid" value="0">Chung</option>'
    else:
        if change == False:
            if forum.subjectpartid != None:
                s= ' <option type="text" name="subjectpartid" value="' + str(forum.subjectpartid.subjectpartid) + ' ">' + forum.subjectpartid.subjectpartname + '</option>'
            else:
                s= '<option type="text" name="subjectpartid" value="0">Chung</option>'
    temp = ''

    for subjectpart in subjectparts: 
        if edit == True and change == False:
            if subjectpart.subjectpartid != forum.subjectpartid.subjectpartid:
                    temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        else:
            temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)