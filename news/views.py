from django.shortcuts import render, redirect
from userdetail.models import News, SubjectPart, Account, Subject
from datetime import datetime
from django.http import JsonResponse
# Create your views here.

def index(request):
    newss = news.objects.all()
    for news in newss:
        news.createdate = news.createdate
        news.editdate = news.editdate
    context = {'newss': newss}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        news = News( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                subjectpartid = SubjectPart.objects.get(subjectpartid = request.POST['subjectpartid']),
                                newsname=request.POST['newsname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        news.save()
        return redirect('/tables_object/')
    else:
        subjectparts = SubjectPart.objects.all()
        for subjectpart in subjectparts:
            subjectpart.createdate = subjectpart.createdate
            subjectpart.editdate = subjectpart.editdate
        
        accounts = Account.objects.all()
        subjects = Subject.objects.all()
        
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate

        for subject in subjects:
            subject.createdate = subject.createdate
            subject.editdate = subject.editdate

        context = {
            'accounts': accounts,
            'subjects': subjects,
            'subjectparts': subjectparts
        }   
       
    return render(request, 'news/news_create.html', context)

def edit(request, id):
    news = News.objects.get(newsid=id)
    news.createdate = news.createdate
    news.editdate = datetime.now()

    subjectparts = SubjectPart.objects.all()
    for subjectpart in subjectparts:
        subjectpart.createdate = subjectpart.createdate
        subjectpart.editdate = subjectpart.editdate

    accounts = Account.objects.all()
    subjects = Subject.objects.all()
        
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate

    context = {
        'accounts': accounts,
        'subjects': subjects,
        'news': news,
        'subjectparts': subjectparts 
    }
   
    return render(request, 'news/news_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    news = News.objects.filter(newsid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    news = News.objects.filter(newsid = id).update(subjectpartid = SubjectPart.objects.get(subjectpartid = getNum(request.POST['subjectpartid'])))
    news = News.objects.get(newsid=id)
    news.newsname=request.POST['newsname']
    news.createdate=news.createdate
    news.editdate=datetime.now()
    news.content=request.POST['content']
    news.isenable=request.POST['isenable']
    news.note=request.POST['note']
    news.save()
    return redirect('/tables_object/')


def delete(request, id):
    news = News.objects.get(newsid= id)
    news.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
def validate_subjectnews(request):
    subject = request.GET.get('subject', None)
    subjectparts = SubjectPart.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        news  = News.objects.get(newsid = request.GET.get('news', None))
        
    if edit == False or change == True:
        s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
    else:
        if change == False:
            s= ' <option type="text" name="subjectpartid" value="' + str(news.subjectpartid.subjectpartid) + ' ">' + news.subjectpartid.subjectpartname + '</option>'
    
    temp = ''

    for subjectpart in subjectparts: 
        if edit == True and change == False:
            if subjectpart.subjectpartid != news.subjectpartid.subjectpartid:
                    temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        else:
            temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)