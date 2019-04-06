from django.shortcuts import render, redirect
from homepage.models import ProjectShareReply, ProjectShare, Account
from datetime import datetime

# Create your views here.

def index(request):
    projectsharereplys = ProjectShareReply.objects.all()
    for projectsharereply in projectsharereplys:
        projectsharereply.createdate = projectsharereply.createdate
        projectsharereply.editdate = projectsharereply.editdate
    context = {'projectsharereplys': projectsharereplys }
    return render(request, 'adminprojectsharereply/projectsharereply_show.html', context)

def create(request):
    if request.method == 'POST':
        projectsharereply = ProjectShareReply( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                projectsharetopicid = ProjectShare.objects.get(projectsharetopicid = request.POST['projectsharetopicid']),
                                content=request.POST['content'],
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        projectsharereply.save()
        return redirect('/adminprojectsharereply/')
    else:
        projectshares = ProjectShare.objects.all()
        for projectshare in projectshares:
            projectshare.createdate = projectshare.createdate
            projectshare.editdate = projectshare.editdate

        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate

        context = {
            'projectshares': projectshares,
            'accounts': accounts,
        }
    return render(request, 'adminprojectsharereply/projectsharereply_create.html', context)

def edit(request, id):
    projectsharereply = ProjectShareReply.objects.get(projectsharereplyid=id)
    projectsharereply.createdate = projectsharereply.createdate
    projectsharereply.editdate = datetime.now()

    projectshares = ProjectShare.objects.all()
    for projectshare in projectshares:
        projectshare.createdate = projectshare.createdate
        projectshare.editdate = projectshare.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    context = {
        'projectsharereply': projectsharereply,
        'projectshares': projectshares,  
        'accounts': accounts,  
    }
    return render(request, 'adminprojectsharereply/projectsharereply_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    projectsharereply = ProjectShareReply.objects.filter(projectsharereplyid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    projectsharereply = ProjectShareReply.objects.filter(projectsharereplyid = id).update(projectsharetopicid = ProjectShare.objects.get(projectsharetopicid = getNum(request.POST['projectsharetopicid'])))
    projectsharereply = ProjectShareReply.objects.get(projectsharereplyid=id)
    projectsharereply.createdate=projectsharereply.createdate
    projectsharereply.editdate=datetime.now()
    projectsharereply.content=request.POST['content']
    projectsharereply.isenable=request.POST['isenable']
    projectsharereply.note=request.POST['note']
    projectsharereply.save()
    return redirect('/adminprojectsharereply/')


def delete(request, id):
    projectsharereply = ProjectShareReply.objects.get(projectsharereplyid= id)
    projectsharereply.delete()
    return redirect('/adminprojectsharereply/')