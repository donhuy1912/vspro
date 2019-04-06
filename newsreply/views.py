from django.shortcuts import render, redirect
from userdetail.models import NewsReply, News, Account
from datetime import datetime

# Create your views here.

def index(request):
    newsreplys = NewsReply.objects.all()
    for newsreply in newsreplys:
        newsreply.createdate = newsreply.createdate
        newsreply.editdate = newsreply.editdate
    context = {'newsreplys': newsreplys }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        newsreply = NewsReply( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                newsid = News.objects.get(newsid = request.POST['newsid']),
                                content=request.POST['content'],
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        newsreply.save()
        return redirect('/tables_relationship/')
    else:
        newss = News.objects.all()
        for news in newss:
            news.createdate = news.createdate
            news.editdate = news.editdate

        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate
        
        context = {
            'newss': newss,
            'accounts': accounts,
        }
    return render(request, 'newsreply/newsreply_create.html', context)

def edit(request, id):
    newsreply = NewsReply.objects.get(newsreplyid=id)
    newsreply.createdate = newsreply.createdate
    newsreply.editdate = datetime.now()

    newss = News.objects.all()
    for news in newss:
        news.createdate = news.createdate
        news.editdate = news.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    context = {
        'newsreply': newsreply,
        'newss': newss,
        'accounts': accounts,
    }
    return render(request, 'newsreply/newsreply_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    newsreply = NewsReply.objects.filter(newsreplyid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    newsreply = NewsReply.objects.filter(newsreplyid = id).update(newsid = News.objects.get(newsid = getNum(request.POST['newsid'])))
    newsreply = NewsReply.objects.get(newsreplyid=id)
    newsreply.createdate=newsreply.createdate
    newsreply.editdate=datetime.now()
    newsreply.content=request.POST['content']
    newsreply.isenable=request.POST['isenable']
    newsreply.note=request.POST['note']
    newsreply.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    newsreply = NewsReply.objects.get(newsreplyid= id)
    newsreply.delete()
    return redirect('/tables_relationship/')