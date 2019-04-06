from django.shortcuts import render, redirect
from userdetail.models import CompetitionSubmittionReply, CompetitionSubmittion, Account, Competition
from datetime import datetime
from django.http import JsonResponse

# Create your views here.

def index(request):
    competitionsubmittionreplys = CompetitionSubmittionReply.objects.all()
    for competitionsubmittionreply in competitionsubmittionreplys:
        competitionsubmittionreply.createdate = competitionsubmittionreply.createdate
        competitionsubmittionreply.editdate = competitionsubmittionreply.editdate
    context = {'competitionsubmittionreplys': competitionsubmittionreplys }
    return render(request, 'adminpage/tables_relationship.html', context)

def create(request):
    if request.method == 'POST':
        competitionsubmittionreply = CompetitionSubmittionReply( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                competitionsubmittionid = CompetitionSubmittion.objects.get(competitionsubmittionid = request.POST['competitionsubmittionid']),
                                content=request.POST['content'],
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        competitionsubmittionreply.save()
        return redirect('/tables_relationship/')
    else:
        competitionsubmittions = CompetitionSubmittion.objects.all()
        for competitionsubmittion in competitionsubmittions:
            competitionsubmittion.createdate = competitionsubmittion.createdate
            competitionsubmittion.editdate = competitionsubmittion.editdate

        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate
        
        competitions = Competition.objects.all()
        for competition in competitions:
            competition.createdate = competition.createdate
            competition.editdate = competition.editdate


    context = {
        'competitionsubmittions': competitionsubmittions,
        'competitions': competitions,
        'accounts': accounts,
    }
    
    return render(request, 'competitionsubmittionreply/competitionsubmittionreply_create.html', context)

def edit(request, id):
    competitionsubmittionreply = CompetitionSubmittionReply.objects.get(competitionsubmittionreplyid=id)
    competitionsubmittionreply.createdate = competitionsubmittionreply.createdate
    competitionsubmittionreply.editdate = datetime.now()

    competitionsubmittions = CompetitionSubmittion.objects.all()
    for competitionsubmittion in competitionsubmittions:
        competitionsubmittion.createdate = competitionsubmittion.createdate
        competitionsubmittion.editdate = competitionsubmittion.editdate

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
        
    competitions = Competition.objects.all()
    for competition in competitions:
        competition.createdate = competition.createdate
        competition.editdate = competition.editdate


    context = {
        'competitionsubmittionreply': competitionsubmittionreply,
        'competitionsubmittions': competitionsubmittions,
        'competitions': competitions,
        'accounts': accounts,
    }
    return render(request, 'competitionsubmittionreply/competitionsubmittionreply_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    competitionsubmittionreply = CompetitionSubmittionReply.objects.filter(competitionsubmittionreplyid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    competitionsubmittionreply = CompetitionSubmittionReply.objects.filter(competitionsubmittionreplyid = id).update(competitionsubmittionid = CompetitionSubmittion.objects.get(competitionsubmittionid = getNum(request.POST['competitionsubmittionid'])))
    competitionsubmittionreply = CompetitionSubmittionReply.objects.get(competitionsubmittionreplyid=id)
    competitionsubmittionreply.createdate=competitionsubmittionreply.createdate
    competitionsubmittionreply.editdate=datetime.now()
    competitionsubmittionreply.content=request.POST['content']
    competitionsubmittionreply.isenable=request.POST['isenable']
    competitionsubmittionreply.note=request.POST['note']
    competitionsubmittionreply.save()
    return redirect('/tables_relationship/')


def delete(request, id):
    competitionsubmittionreply = CompetitionSubmittionReply.objects.get(competitionsubmittionreplyid= id)
    competitionsubmittionreply.delete()
    return redirect('/tables_relationship/')


#lấy giá trị competition được nhập vào để giới hạn giá trị show ra của competitionsubmittion
# def validate_competitioncompetitionsubmittionreply(request):
#     competition = request.GET.get('competition', None)
#     competitionsubmittions = CompetitionSubmittion.objects.filter(competitionid = competition)
#     s = '<option type="text" name="competitionsubmittionid" value="">-- Chọn --</option>'
#     temp = ''
#     for competitionsubmittion in competitionsubmittions:
#         temp = '<option type="text" name="competitionsubmittionid" value=" ' + str(competitionsubmittion.competitionsubmittionid) + ' "> ' + competitionsubmittion.description + ' </option>'
#         s+=temp
#     data = {
#         'is_taken': s
#     }
#     return JsonResponse(data)


def validate_competitioncompetitionsubmittionreply(request):
    competition = request.GET.get('competition', None)
    competitionsubmittions = CompetitionSubmittion.objects.filter(competitionid=competition)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
    
    if edit == True:
        competitionsubmittionreply  = CompetitionSubmittionReply.objects.get(competitionsubmittionreplyid = request.GET.get('competitionsubmittionreply', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="competitionsubmittionid" value="">-- Chọn --</option>'
    else:
        if change == False:
            s= ' <option type="text" name="competitionsubmittionid" value="' + str(competitionsubmittionreply.competitionsubmittionid.competitionsubmittionid) + ' ">' + competitionsubmittionreply.competitionsubmittionid.description + '</option>'
    temp = ''

    for competitionsubmittion in competitionsubmittions: 
        if edit == True and change == False:
            if competitionsubmittion.competitionsubmittionid != competitionsubmittionreply.competitionsubmittionid.competitionsubmittionid:
                    temp = ' <option type="text" name="competitionsubmittionid" value="' + str(competitionsubmittion.competitionsubmittionid) + ' ">' + competitionsubmittion.description + '</option>'
        else:
            temp = ' <option type="text" name="competitionsubmittionid" value="' + str(competitionsubmittion.competitionsubmittionid) + ' ">' + competitionsubmittion.description + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)