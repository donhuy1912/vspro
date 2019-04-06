from django.shortcuts import render, redirect
from userdetail.models import ForumReply, Forum, Account
from datetime import datetime

# Create your views here.

def index(request):
    forumreplys = ForumReply.objects.all()
    for forumreply in forumreplys:
        forumreply.createdate = forumreply.createdate
        forumreply.editdate = forumreply.editdate
    context = {'forumreplys': forumreplys }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        forumreply = ForumReply( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                forumtopicid = Forum.objects.get(forumtopicid = request.POST['forumid']),
                                content=request.POST['content'],
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        forumreply.save()
        return redirect('/tables_relationship/')
    else:
        forums = Forum.objects.all()
        for forum in forums:
            forum.createdate = forum.createdate
            forum.editdate = forum.editdate

        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate

        context = {
            'forums': forums,
            'accounts': accounts,
        }
    return render(request, 'forumreply/forumreply_create.html', context)

def edit(request, id):
    forumreply = ForumReply.objects.get(forumreplyid=id)
    forumreply.createdate = forumreply.createdate
    forumreply.editdate = datetime.now()

    forums = Forum.objects.all()
    for forum in forums:
        forum.createdate = forum.createdate
        forum.editdate = forum.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    context = {
        'forumreply': forumreply,
        'forums': forums,
        'accounts': accounts,
    }
    return render(request, 'forumreply/forumreply_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    forumreply = ForumReply.objects.filter(forumreplyid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    forumreply = ForumReply.objects.filter(forumreplyid = id).update(forumtopicid = Forum.objects.get(forumtopicid = getNum(request.POST['forumid'])))
    forumreply = ForumReply.objects.get(forumreplyid=id)
    forumreply.createdate=forumreply.createdate
    forumreply.editdate=datetime.now()
    forumreply.status=request.POST['content']
    forumreply.isenable=request.POST['isenable']
    forumreply.note=request.POST['note']
    forumreply.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    forumreply = ForumReply.objects.get(forumreplyid= id)
    forumreply.delete()
    return redirect('/tables_relationship/')