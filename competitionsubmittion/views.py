from django.shortcuts import render, redirect
from userdetail.models import CompetitionSubmittion, Competition, Account, SubjectPart, Subject
from datetime import datetime
from homepage.myfunction import tokenFile
from django.http import JsonResponse
# Create your views here.

def index(request):
    competitionsubmittions = CompetitionSubmittion.objects.all()
    for competitionsubmittion in competitionsubmittions:
        competitionsubmittion.createdate = competitionsubmittion.createdate
        competitionsubmittion.editdate = competitionsubmittion.editdate
    context = {'competitionsubmittions': competitionsubmittions}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        try:
            token_link = request.FILES['link']
        except:
            token_link = None
        lin = ''
        if token_link != None:
            lin = tokenFile(token_link)
        competitionsubmittion = CompetitionSubmittion( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                competitionid = Competition.objects.get(competitionid = request.POST['competitionid']),
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                link=lin,
                                description=request.POST['description'],
                                content=request.POST['content'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        competitionsubmittion.save()
        return redirect('/tables_object/')
    else:
        competitions = Competition.objects.all()
        for competition in competitions:
            competition.createdate = competition.createdate
            competition.editdate = competition.editdate
            competition.opendate = competition.opendate.strftime("%Y-%m-%d %H:%M:%S")
            competition.enddate = competition.enddate.strftime("%Y-%m-%d %H:%M:%S")
        
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
            'competitions': competitions
        }
       
    return render(request, 'competitionsubmittion/competitionsubmittion_create.html', context)

def edit(request, id):
    competitionsubmittion = CompetitionSubmittion.objects.get(competitionsubmittionid=id)
    competitionsubmittion.createdate = competitionsubmittion.createdate
    competitionsubmittion.editdate = datetime.now()


    competitions = Competition.objects.all()
    for competition in competitions:
        competition.createdate = competition.createdate
        competition.editdate = competition.editdate
        competition.opendate = competition.opendate.strftime("%Y-%m-%d %H:%M:%S")
        competition.enddate = competition.enddate.strftime("%Y-%m-%d %H:%M:%S")
    
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
        'competitionsubmittion': competitionsubmittion,
        'competitions': competitions
    }
   
    return render(request, 'competitionsubmittion/competitionsubmittion_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    competitionsubmittion = CompetitionSubmittion.objects.filter(competitionsubmittionid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    competitionsubmittion = CompetitionSubmittion.objects.filter(competitionsubmittionid = id).update(competitionid = Competition.objects.get(competitionid = getNum(request.POST['competitionid'])))
    competitionsubmittion = CompetitionSubmittion.objects.get(competitionsubmittionid=id)
    competitionsubmittion.createdate=competitionsubmittion.createdate
    competitionsubmittion.editdate=datetime.now()
    competitionsubmittion.link=request.POST['link']
    competitionsubmittion.description=request.POST['description']
    competitionsubmittion.content=request.POST['content']
    competitionsubmittion.isenable=request.POST['isenable']
    competitionsubmittion.note=request.POST['note']
    competitionsubmittion.save()
    return redirect('/tables_object/')


def delete(request, id):
    competitionsubmittion = CompetitionSubmittion.objects.get(competitionsubmittionid= id)
    competitionsubmittion.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
# def validate_subjectcompetitionsubmittion(request):
#     subject = request.GET.get('subject',None)
#     subjectparts = SubjectPart.objects.filter(subjectid = subject)
#     s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
#     temp = ''
#     for subjectpart in subjectparts:
#         temp = '<option type="text" name="subjectpartid" value=" ' + str(subjectpart.subjectpartid) + ' "> ' + subjectpart.subjectpartname + ' </option'
#         s+=temp
#     data = {
#         'is_taken': s
#     }
#     return JsonResponse(data)

# def validate_subjectcompetitionsubmittion(request):
#     subject = request.GET.get('subject', None)
#     subjectparts = SubjectPart.objects.filter(subjectid=subject)
#     edit = request.GET.get('edit', False)
#     if edit == '1': 
#         edit = True
    
#     change = request.GET.get('change', False)
#     if change == '1': 
#         change = True
        
#     if edit == True:
#         competitionsubmittion  = CompetitionSubmittion.objects.get(competitionsubmittionid = request.GET.get('competitionsubmittion', None))
    
#     if edit == False or change == True:
#         s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
#     else:
#         if change == False:
#             s= ' <option type="text" name="subjectpartid" value="' + str(competitionsubmittion.competitionid.subjectpartid.subjectpartid) + ' ">' + competitionsubmittion.competitionid.subjectpartid.subjectpartname + '</option>'
    
#     temp = ''

#     for subjectpart in subjectparts: 
#         if edit == True and change == False:
#             if subjectpart.subjectpartid != competitionsubmittion.competitionid.subjectpartid.subjectpartid:
#                     temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
#         else:
#             temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
#         s = s+temp

#     data = {
#         'is_taken': s
#     }

#     return JsonResponse(data)\


def validate_subjectcompetitionsubmittion(request):
    subject = request.GET.get('subject', None)
    subjectparts = SubjectPart.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        competitionsubmittion  = CompetitionSubmittion.objects.get(competitionsubmittionid = request.GET.get('competitionsubmittion', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="subjectpartid" value="">-- Chọn --</option>'
        if(subject == "0"):
            s = '<option type="text" name="subjectpartid" value="0">Chung</option>'
    else:
        if change == False:
            if competitionsubmittion.subjectpartid != None:
                s= ' <option type="text" name="subjectpartid" value="' + str(competitionsubmittion.subjectpartid.subjectpartid) + ' ">' + competitionsubmittion.subjectpartid.subjectpartname + '</option>'
            else:
                s= '<option type="text" name="subjectpartid" value="0">Chung</option>'
    temp = ''

    for subjectpart in subjectparts: 
        if edit == True and change == False:
            if subjectpart.subjectpartid != competitionsubmittion.subjectpartid.subjectpartid:
                    temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        else:
            temp = ' <option type="text" name="subjectpartid" value="' + str(subjectpart.subjectpartid) + ' ">' + subjectpart.subjectpartname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)

#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của subjectpart
# def validate_subjectpartcompetitionsubmittion(request):
#     subjectpart = request.GET.get('subjectpart',None)
#     competitions = Competition.objects.filter(subjectpartid = subjectpart)
#     s = '<option type="text" name="competitionid" value="">-- Chọn --</option>'
#     temp = ''
#     for competition in competitions:
#         temp = '<option type="text" name="competitionid" value=" ' + str(competition.competitionid) + ' "> ' + competition.competitionname + ' </option'
#         s+=temp
#     data = {
#         'is_taken': s
#     }
#     return JsonResponse(data)


def validate_subjectpartcompetitionsubmittion(request):
    subjectpart = request.GET.get('subjectpart', None)
    if subjectpart == '0':
        subjectpart = None
    competitions = Competition.objects.filter(subjectpartid=subjectpart)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        competitionsubmittion  = CompetitionSubmittion.objects.get(competitionsubmittionid = request.GET.get('competitionsubmittion', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="competitionid" value="">-- Chọn --</option>'
    else:
        if change == False:
            s= ' <option type="text" name="competitionid" value="' + str(competitionsubmittion.competitionid.competitionid) + ' ">' + competitionsubmittion.competitionid.competitionname + '</option>'
    
    temp = ''

    for competition in competitions: 
        if edit == True and change == False:
            if competition.competitionid != competitionsubmittion.competitionid.competitionid:
                    temp = ' <option type="text" name="competitionid" value="' + str(competition.competitionid) + ' ">' + competition.competitionname + '</option>'
        else:
            temp = ' <option type="text" name="competitionid" value="' + str(competition.competitionid) + ' ">' + competition.competitionname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)

