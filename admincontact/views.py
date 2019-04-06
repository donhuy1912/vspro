from django.shortcuts import render, redirect
from homepage.models import Account, Contact
from datetime import datetime

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    for contact in contacts:
        contact.createdate = contact.createdate
        
    context = {'contacts': contacts}
    return render(request, 'admincontact/contact_show.html', context)

def create(request):
    if request.method == 'POST':
        contact = Contact( 
                                accountid=Account.objects.get(accountid = request.POST['accountid']), 
                                createdate= datetime.now(), 
                                content= request.POST['content'], 
                                note=request.POST['note'])
        contact.save()
        return redirect('/admincontact/')
    else:
        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate
        context = {'accounts': accounts}
    return render(request, 'admincontact/contact_create.html', context)

def edit(request, id):
    contact = Contact.objects.get(contactid=id)
    contact.createdate = contact.createdate
    
    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
    
    context = {
        'contact': contact,
        'accounts': accounts,    
    }

    return render(request, 'admincontact/contact_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def update(request, id):
    contact = Contact.objects.get(contactid=id)
    contact.accountid=Account.objects.get(accountid = request.POST['accountid'])
    contact.createdate=contact.createdate
    contact.content=request.POST['content']
    contact.note=request.POST['note']
    contact.save()
    return redirect('/admincontact/')


def delete(request, id):
    contact = Contact.objects.get(contactid= id)
    contact.delete()
    return redirect('/admincontact/')