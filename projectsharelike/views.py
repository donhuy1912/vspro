from django.shortcuts import render, redirect
from userdetail.models import ProjectShareLike, ProjectShare, Account
from datetime import datetime

# Create your views here.

def index(request):
    projectsharelikes = ProjectShareLike.objects.all()
    for projectsharelike in projectsharelikes:
        projectsharelike.createdate = projectsharelike.createdate
        projectsharelike.editdate = projectsharelike.editdate
    context = {'projectsharelikes': projectsharelikes }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        projectsharelike = ProjectShareLike( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                projectsharetopicid = ProjectShare.objects.get(projectsharetopicid = request.POST['projectsharetopicid']),
                                status=request.POST['status'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        projectsharelike.save()
        return redirect('/tables_relationship/')
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
    return render(request, 'projectsharelike/projectsharelike_create.html', context)

def edit(request, id):
    projectsharelike = ProjectShareLike.objects.get(projectsharelikeid=id)

    projectshares = ProjectShare.objects.all()
    for projectshare in projectshares:
        projectshare.createdate = projectshare.createdate
        projectshare.editdate = projectshare.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    context = {
        'projectsharelike': projectsharelike,
        'projectshares': projectshares,
        'accounts': accounts,
    }
    return render(request, 'projectsharelike/projectsharelike_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    projectsharelike = ProjectShareLike.objects.filter(projectsharelikeid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    projectsharelike = ProjectShareLike.objects.filter(projectsharelikeid = id).update(projectsharetopicid = ProjectShare.objects.get(projectsharetopicid = getNum(request.POST['projectsharetopicid'])))
    projectsharelike = ProjectShareLike.objects.get(projectsharelikeid=id)
    projectsharelike.status=request.POST['status']
    projectsharelike.isenable=request.POST['isenable']
    projectsharelike.note=request.POST['note']
    projectsharelike.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    projectsharelike = ProjectShareLike.objects.get(projectsharelikeid= id)
    projectsharelike.delete()
    return redirect('/tables_relationship/')