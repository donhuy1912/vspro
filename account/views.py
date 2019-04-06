from django.shortcuts import render, redirect
#from userdetail.models import Account, AccountType
from userdetail.models import *
from datetime import datetime
from homepage.myfunction import *
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
# def admin1 (request):
#     return render(request, 'account/account_create.html')

def index(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'adminpage/tables_object.html', context)
    


def create(request):
    # if request.method == 'POST':
    #     # Lấy avatar
    #     try:
    #         token_avatar = request.FILES['avatar']
    #     except:
    #         token_avatar = None
    #     ava = ''
    #     if tokenFile(token_avatar) != None:
    #         ava = tokenFile(token_avatar)
            
    #     account = Account( 
    #                             accounttypeid = AccountType.objects.get(accounttypeid = request.POST['accounttypeid']),
    #                             username = request.POST['username'],
    #                             password = hashPassword(request.POST['password']), 
    #                             createdate =  datetime.now(), 
    #                             editdate =  datetime.now(),
    #                             # avatar = request.POST['avatar'],
    #                             avatar = ava,
    #                             resetcode = request.POST['resetcode'],
    #                             isenable = request.POST['isenable'],  
    #                             note = request.POST['note'])
    #     account.save()
    #     return redirect('/tables_object/')
    #     #return redirect('/crud/')
    #     # accounttypeid = request.POST['accounttypeid'],
    # else:
    #     accounttypes = AccountType.objects.all()
    #     context = {'accounttypes': accounttypes}
    # return render(request, 'account/ac
    accounttypes = AccountType.objects.all()
    context = {'accounttypes': accounttypes}

    if request.method == "POST":
        accounttypeid = request.POST.get('accounttypeid')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # resetcode = request.POST.get('resetcode')
        isenable = request.POST.get('isenable') 
        note = request.POST.get('note')
        
        if (boolcheckSpace(username) or boolcheckSpace(password1)):
            messages.error(request, 'Không được có khoảng trắng trong tên đăng nhập hoặc mật khẩu')
            return render(request, 'account/account_create.html', context)
        elif boolcheckUser(username):
            messages.error(request, 'Tên đăng nhập đã tồn tại')
            return render(request, 'account/account_create.html', context)
        elif not (boolcheckPassword(password1)):
            messages.error(request, 'Mật khẩu phải dài hơn 8 ký tự bao gồm chữ hoa, chữ thường và số')
            return render(request, 'account/account_create.html', context)
        elif (password1 != password2):
            messages.error(request, 'Mật khẩu không trùng khớp')
            return render(request, 'account/account_create.html', context)
        else:
            # Lấy avatar
            try:
                token_avatar = request.FILES['avatar']
            except:
                token_avatar = None
            ava = ''
            if tokenFile(token_avatar) != None:
                ava = tokenFile(token_avatar)
                        
            account = Account( 
                                accounttypeid = AccountType.objects.get(accounttypeid =  accounttypeid),
                                username = username,
                                password = hashPassword(password1), 
                                createdate =  datetime.now(), 
                                editdate =  datetime.now(),
                                avatar = ava,
                                # resetcode = resetcode,
                                isenable = isenable,  
                                note =  note)
            account.save()
            return redirect('/tables_object/')
            #return redirect('/crud/')
            # accounttypeid = request.POST['accounttypeid'],
           
    return render(request, 'account/account_create.html', context)

def edit(request, id):
    account = Account.objects.get(accountid = id)
    account.createdate = account.createdate
    account.editdate = datetime.now()


    accounttypes = AccountType.objects.all()
    
    context = {'account': account,
               'accounttypes': accounttypes}
    return render(request, 'account/account_edit.html', context)

def us_date_to_iso(us_date):
    return '{2}-{0:>02}-{1:>02}'.format(*us_date.split('/'))

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
    context = {
        'accounts': accounts
    }

    account = Account.objects.get(accountid = id)
    if request.method == 'POST':
        accounttypeid = request.POST.get('accounttypeid')
        username = request.POST.get('username')
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        # resetcode = request.POST.get('resetcode')
        avatar = request.POST['avatar']
        isenable = request.POST.get('isenable') 
        note = request.POST.get('note')
        
        if boolcheckSpace(username):
            messages.error(request, 'Không được có khoảng trắng trong tên đăng nhập hoặc mật khẩu')
            return redirect('/tables_object/account/edit/'+id)
        elif (account.username != username and boolcheckUser(username)):
            messages.error(request, 'Tên đăng nhập đã tồn tại')
            return redirect('/tables_object/account/edit/'+id)
        # elif account.password != password1 and (not (boolcheckPassword(password1))):
        #     messages.error(request, 'Mật khẩu phải dài hơn 8 ký tự bao gồm chữ hoa, chữ thường và số')
        #     return redirect('/tables_object/account/edit/'+id)
        # elif password1 != password2:
        #     messages.error(request, 'Mật khẩu không trùng khớp')
        #     return redirect('/tables_object/account/edit/'+id)
        else:
            # try:
            #     token_avatar = request.FILES['avatar']
            # except:
            #     token_avatar = None
            # ava = ''
            # if token_avatar != None:
            #     ava = tokenFile(token_avatar)
            account = Account.objects.filter(accountid = id).update(accounttypeid = AccountType.objects.get(accounttypeid = getNum(accounttypeid)))
            account = Account.objects.get(accountid = id)
            if account.username != username:
                account.username = username
            # if account.password != password1:
            #     account.password = hashPassword(password1)
            account.createdate = account.createdate
            account.editdate = datetime.now()
            account.avatar = avatar
            # account.resetcode = resetcode
            account.isenable = isenable
            account.note = note
            account.save()
            return redirect('/tables_object/')
    return render(request, 'account/account_edit.html', context)
    
def delete(request, id):
    account = Account.objects.get(accountid =  id)
    account.delete()
    return redirect('/tables_object/')