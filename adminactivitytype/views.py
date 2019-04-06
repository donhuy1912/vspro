from django.shortcuts import render, redirect
from homepage.models import ActivityType
from datetime import datetime

# Create your views here.

def index(request):
    activitytypes = ActivityType.objects.all()
    for activitytype in activitytypes:
        #activitytype.createdate = activitytype.createdate.strftime("%Y-%m-%d")
        activitytype.createdate = activitytype.createdate
        activitytype.editdate = activitytype.editdate

    context = {'activitytypes': activitytypes}
    return render(request, 'adminactivitytype/activitytype_show.html', context)

def create(request):
    if request.method == 'POST':
        activitytype = ActivityType( 
                                activitytypename=request.POST['activitytypename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        activitytype.save()
        return redirect('/adminactivitytype/')
       
    return render(request, 'adminactivitytype/activitytype_create.html')

def edit(request, id):
    activitytype = ActivityType.objects.get(activitytypeid=id)
    activitytype.createdate = activitytype.createdate
    activitytype.editdate = datetime.now()
    context = {'activitytype': activitytype}
    return render(request, 'adminactivitytype/activitytype_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def update(request, id):
    activitytype = ActivityType.objects.get(activitytypeid=id)
    activitytype.activitytypename=request.POST['activitytypename']
    activitytype.createdate=activitytype.createdate
    activitytype.editdate=datetime.now()
    activitytype.isenable=request.POST['isenable']
    activitytype.note=request.POST['note']
    activitytype.save()
    return redirect('/adminactivitytype/')


def delete(request, id):
    activitytype = ActivityType.objects.get(activitytypeid= id)
    activitytype.delete()
    return redirect('/adminactivitytype/')