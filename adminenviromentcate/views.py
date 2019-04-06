from django.shortcuts import render, redirect
from homepage.models import EnviromentCate
from datetime import datetime

# Create your views here.

def index(request):
    enviromentcates = EnviromentCate.objects.all()
    for enviromentcate in enviromentcates:
        enviromentcate.createdate = enviromentcate.createdate
        enviromentcate.editdate = enviromentcate.editdate

    context = {'enviromentcates': enviromentcates}
    return render(request, 'adminenviromentcate/enviromentcate_show.html', context)

def create(request):
    if request.method == 'POST':
        enviromentcate = EnviromentCate( 
                                enviromentcatename=request.POST['enviromentcatename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        enviromentcate.save()
        return redirect('/adminenviromentcate/')

    return render(request, 'adminenviromentcate/enviromentcate_create.html')

def edit(request, id):
    enviromentcate = EnviromentCate.objects.get(enviromentcateid=id)
    enviromentcate.createdate = enviromentcate.createdate
    enviromentcate.editdate = datetime.now()
    context = {'enviromentcate': enviromentcate}
    return render(request, 'adminenviromentcate/enviromentcate_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def update(request, id):
    enviromentcate = EnviromentCate.objects.get(enviromentcateid=id)
    enviromentcate.enviromentcatename=request.POST['enviromentcatename']
    enviromentcate.createdate=enviromentcate.createdate
    enviromentcate.editdate=datetime.now()
    enviromentcate.isenable=request.POST['isenable']
    enviromentcate.note=request.POST['note']
    enviromentcate.save()
    return redirect('/adminenviromentcate/')


def delete(request, id):
    enviromentcate = EnviromentCate.objects.get(enviromentcateid= id)
    enviromentcate.delete()
    return redirect('/adminenviromentcate/')