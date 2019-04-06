from django.shortcuts import render, redirect
from userdetail.models import ForumLike, Forum, Account 
from datetime import datetime

# Create your views here.

def index(request):
    forumlikes = ForumLike.objects.all()
    for forumlike in forumlikes:
        forumlike.createdate = forumlike.createdate
        forumlike.editdate = forumlike.editdate
    context = {'forumlikes': forumlikes }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        forumlike = ForumLike( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                forumtopicid = Forum.objects.get(forumtopicid = request.POST['forumid']),
                                status=request.POST['status'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        forumlike.save()
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
            'accounts': accounts
        }
    return render(request, 'forumlike/forumlike_create.html', context)

def edit(request, id):
    forumlike = ForumLike.objects.get(forumlikeid=id)
    forums = Forum.objects.all()
    for forum in forums:
        forum.createdate = forum.createdate
        forum.editdate = forum.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    context = {
        'forumlike': forumlike,
        'forums': forums,
        'accounts': accounts,
    }
    return render(request, 'forumlike/forumlike_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    forumlike = ForumLike.objects.filter(forumlikeid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    forumlike = ForumLike.objects.filter(forumlikeid = id).update(forumtopicid = Forum.objects.get(forumtopicid = getNum(request.POST['forumid'])))
    forumlike = ForumLike.objects.get(forumlikeid=id)
    forumlike.status=request.POST['status']
    forumlike.isenable=request.POST['isenable']
    forumlike.note=request.POST['note']
    forumlike.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    forumlike = ForumLike.objects.get(forumlikeid= id)
    forumlike.delete()
    return redirect('/tables_relationship/')