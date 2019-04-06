from django.shortcuts import render, redirect
from homepage.models import ForumLike, Forum, Account 
from datetime import datetime

# Create your views here.

def index(request):
    forumlikes = ForumLike.objects.all()
    
    context = {'forumlikes': forumlikes }
    return render(request, 'adminforumlike/forumlike_show.html', context)

def create(request):
    if request.method == 'POST':
        forumlike = ForumLike( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                forumtopicid = Forum.objects.get(forumtopicid = request.POST['forumid']),
                                status=request.POST['status'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        forumlike.save()
        return redirect('/adminforumlike/')
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
    return render(request, 'adminforumlike/forumlike_create.html', context)

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
    return render(request, 'adminforumlike/forumlike_edit.html', context)

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
    return redirect('/adminforumlike/')


def delete(request, id):
    forumlike = ForumLike.objects.get(forumlikeid= id)
    forumlike.delete()
    return redirect('/adminforumlike/')