from django.shortcuts import render, redirect
from homepage.models import GameType
from datetime import datetime

# Create your views here.

def index(request):
    gametypes = GameType.objects.all()
    for gametype in gametypes:
        gametype.createdate = gametype.createdate
        gametype.editdate = gametype.editdate

    context = {'gametypes': gametypes}
    return render(request, 'admingametype/gametype_show.html', context)

def create(request):
    if request.method == 'POST':
        gametype = GameType( 
                                gametypename=request.POST['gametypename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now())
        gametype.save()
        return redirect('/admingametype/')

    return render(request, 'admingametype/gametype_create.html')

def edit(request, id):
    gametype = GameType.objects.get(gametypeid=id)
    gametype.createdate = gametype.createdate
    gametype.editdate = datetime.now()
    context = {'gametype': gametype}
    return render(request, 'admingametype/gametype_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def update(request, id):
    gametype = GameType.objects.get(gametypeid=id)
    gametype.gametypename=request.POST['gametypename']
    gametype.createdate=gametype.createdate
    gametype.editdate=datetime.now()
    gametype.save()
    return redirect('/admingametype/')


def delete(request, id):
    gametype = GameType.objects.get(gametypeid= id)
    gametype.delete()
    return redirect('/admingametype/')