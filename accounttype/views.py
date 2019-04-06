from django.shortcuts import render, redirect
from userdetail.models import AccountType
from datetime import datetime

# Create your views here.

def index(request):
    accounttypes = AccountType.objects.all()
    for accounttype in accounttypes:
        #accounttype.createdate = accounttype.createdate.strftime("%Y-%m-%d")
        accounttype.createdate = accounttype.createdate
        accounttype.editdate = accounttype.editdate

    context = {'accounttypes': accounttypes}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        accounttype = AccountType( 
                                accounttypename=request.POST['accounttypename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        accounttype.save()
        return redirect('/tables_object/')
        #return redirect('/crud/')
        # accounttypeid = request.POST['accounttypeid'],
    return render(request, 'accounttype/accounttype_create.html')

def edit(request, id):
    accounttype = AccountType.objects.get(accounttypeid=id)
    accounttype.createdate = accounttype.createdate
    accounttype.editdate = datetime.now()
    context = {'accounttype': accounttype}
    return render(request, 'accounttype/accounttype_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def update(request, id):
    accounttype = AccountType.objects.get(accounttypeid=id)
    accounttype.accounttypename=request.POST['accounttypename']
    accounttype.createdate=accounttype.createdate
    accounttype.editdate=datetime.now()
    accounttype.isenable=request.POST['isenable']
    accounttype.note=request.POST['note']

    # accounttype.accounttypename = request.POST['accounttypename']
    # accounttype.createdate = request.POST['createdate']
    accounttype.save()
    return redirect('/tables_object/')
    #return redirect('/crud/')


def delete(request, id):
    accounttype = AccountType.objects.get(accounttypeid= id)
    accounttype.delete()
    return redirect('/tables_object/')
    #return redirect('/crud/')