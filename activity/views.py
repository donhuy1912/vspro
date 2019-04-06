from django.shortcuts import render, redirect
from userdetail.models import Activity, ActivityType, Item, Account
from datetime import datetime
from homepage.myfunction import *
from django.http import JsonResponse
# Create your views here.

def index(request):
    activitys = Activity.objects.all()
    for activity in activitys:
        activity.createdate = activity.createdate
        activity.editdate = activity.editdate
    context = {'activitys': activitys}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        if request.POST['activityid'] == '':
            requiredactivityid = None
        else:
            requiredactivityid = Activity.objects.get(activityid = request.POST['activityid'])
        try:
            token_link = request.FILES['link']
        except:
            token_link = None
        lin = ''
        if token_link != None:
            lin = tokenFile(token_link)
        activity = Activity( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                requiredactivityid = requiredactivityid,
                                itemid = Item.objects.get(itemid = request.POST['itemid']),
                                activitytypeid = ActivityType.objects.get(activitytypeid = request.POST['activitytypeid']),
                                activityname=request.POST['activityname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                time = request.POST['time'],
                                description=request.POST['description'],
                                content=request.POST['content'],
                                order=request.POST['order'],
                                link=lin,
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        activity.save()
        return redirect('/tables_object/')
    else:
        activitys = Activity.objects.all()
        for activity in activitys:
            activity.createdate = activity.createdate
            activity.editdate = activity.editdate
        
        accounts = Account.objects.all()
        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate
        
        subjects = Subject.objects.all()
        for subject in subjects:
            subject.createdate = subject.createdate
            subject.editdate = subject.editdate

        items = Item.objects.all()
        for item in items:
            item.createdate = item.createdate
            item.editdate = item.editdate
        
        activitytypes = ActivityType.objects.all()
        for activitytype in activitytypes:
            activitytype.createdate = activitytype.createdate
            activitytype.editdate = activitytype.editdate
        context = {'activitys': activitys,
                'activitytypes': activitytypes,
                'accounts': accounts,
                'items': items,
                'subjects': subjects,
        }
    return render(request, 'activity/activity_create.html', context)

def edit(request, id):
    # try:
    #     token_link = request.FILES['link']
    # except:
    #     token_link = None
    # lin = ''
    # if token_link != None:
    #     lin = tokenFile(token_link)
    activity = Activity.objects.get(activityid=id)
    activity.link = activity.link
    # activity.link = lin

    activity.createdate = activity.createdate
    activity.editdate = datetime.now()
    activitys = Activity.objects.all()
    items = Item.objects.all()
    activitytypes = ActivityType.objects.all()
    subjectid = activity.itemid.lessonid.chapterid.subjectid
    
    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
        
    subjects = Subject.objects.all()
    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate

    context = {
        'activity': activity,
        'activitys': activitys,
        'activitytypes': activitytypes,
        'items': items,
        'subjects': subjects,
        'accounts': accounts,
        'subjectid': subjectid
    }
    return render(request, 'activity/activity_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    # try:
    #     token_link = request.FILES['link']
    # except:
    #     token_link = None
    # lin = ''
    # if token_link != None:
    #     lin = tokenFile(token_link)
    
    activity = Activity.objects.filter(activityid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    if request.POST['activityid'] != '' and request.POST['activityid'] != 'None':
        activity = Activity.objects.filter(activityid = id).update(requiredactivityid = Activity.objects.get(activityid = getNum(request.POST['activityid'])))
    else:
        Activity.objects.filter(activityid = id).update(requiredactivityid = None)
    
    activity = Activity.objects.filter(activityid = id).update(itemid = Item.objects.get(itemid = getNum(request.POST['itemid'])))
    activity = Activity.objects.filter(activityid = id).update(activitytypeid = ActivityType.objects.get(activitytypeid = getNum(request.POST['activitytypeid'])))
    activity = Activity.objects.get(activityid=id)
    activity.activityname=request.POST['activityname']
    activity.createdate=activity.createdate
    activity.editdate=datetime.now()
    activity.time = request.POST['time']
    activity.description=request.POST['description']
    activity.content=request.POST['content']
    activity.order=request.POST['order']
    activity.link=request.POST['link']
    activity.isenable=request.POST['isenable']
    activity.note=request.POST['note']
    activity.save()
    return redirect('/tables_object/')


def delete(request, id):
    activity = Activity.objects.get(activityid= id)
    activity.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của chapter
def validate_subjectactivity(request):
    subject = request.GET.get('subject', None)
    chapters = Chapter.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        activity  = Activity.objects.get(activityid = request.GET.get('activity', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="chapterid" value="">-- Chọn --</option>'
    else:
        if change == False:
            s= ' <option type="text" name="chapterid" value="' + str(activity.itemid.lessonid.chapterid.chapterid) + ' ">' + activity.itemid.lessonid.chapterid.chaptername + '</option>'
    
    temp = ''

    for chapter in chapters: 
        if edit == True and change == False:
            if chapter.chapterid != activity.itemid.lessonid.chapterid.chapterid:
                    temp = ' <option type="text" name="chapterid" value="' + str(chapter.chapterid) + ' ">' + chapter.chaptername + '</option>'
        else:
            temp = ' <option type="text" name="chapterid" value="' + str(chapter.chapterid) + ' ">' + chapter.chaptername + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)




#lấy giá trị chapter được nhập vào để giới hạn giá trị show ra của lesson
def validate_chapteractivity(request):
    chapter = request.GET.get('chapter', None)
    lessons = Lesson.objects.filter(chapterid=chapter)
    
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True

    if edit == True:
        activity  = Activity.objects.get(activityid = request.GET.get('activity', None))

    if edit == False or change == True:
        s = '<option type="text" name="lessonid" value="">-- Chọn --</option>'
    else:
        s= ' <option type="text" name="lessonid" value="' + str(activity.itemid.lessonid.lessonid) + ' ">' + activity.itemid.lessonid.lessonname + '</option>'
    
    temp = ''

    for lesson in lessons: 
        if edit == True and change == False:
            if lesson.lessonid!=activity.itemid.lessonid.lessonid:
                    temp = ' <option type="text" name="lessonid" value="' + str(lesson.lessonid) + ' ">' + lesson.lessonname + '</option>'
        else:
            temp = ' <option type="text" name="lessonid" value="' + str(lesson.lessonid) + ' ">' + lesson.lessonname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)

#lấy giá trị lesson được nhập vào để giới hạn giá trị show ra của item
def validate_lessonactivity(request):
    lesson = request.GET.get('lesson', None)
    items = Item.objects.filter(lessonid=lesson)
    
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True

    if edit == True:
        activity  = Activity.objects.get(activityid = request.GET.get('activity', None))

    if edit == False or change == True:
        s = '<option type="text" name="itemid" value="">-- Chọn --</option>'
    else:
        s= ' <option type="text" name="itemid" value="' + str(activity.itemid.itemid) + ' ">' + activity.itemid.itemname + '</option>'
    
    temp = ''

    for item in items: 
        if edit == True and change == False:
            if item.itemid!=activity.itemid.itemid:
                    temp = ' <option type="text" name="itemid" value="' + str(item.itemid) + ' ">' + item.itemname + '</option>'
        else:
            temp = ' <option type="text" name="itemid" value="' + str(item.itemid) + ' ">' + item.itemname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)

#lấy giá trị lesson được nhập vào để giới hạn giá trị show ra của activity
def validate_lessonactivityactivity(request):
    lesson = request.GET.get('lesson', None)
    items = Item.objects.filter(lessonid=lesson)
    
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True

    if edit == True:
        act  = Activity.objects.get(activityid = request.GET.get('activity', None))
       

    if edit == False or change == True:
        s = '<option type="text" name="activityid" value="">-- Chọn --</option>'
        if edit == False:
            s += '<option type="text" name="activityid" value="">-- Không có --</option>'
    else:
        if act.requiredactivityid == None:
            s ='<option type="text" name="activityid" value="">-- Không có --</option>'   
        else:
            s= ' <option type="text" name="activityid" value="' + str(act.requiredactivityid.activityid) + ' ">' + act.requiredactivityid.activityname + '</option>'
    
    temp = ''

    for item in items: 
        activitys = Activity.objects.filter(itemid = item.itemid)
        for activity in activitys:
            if edit == True and change == False:
                if act.requiredactivityid != None and activity.activityid != act.requiredactivityid.activityid:
                   temp = '<option type="text" name="activityid" value="' + str(activity.activityid) + ' ">' + activity.activityname + '</option>'
            else:
                temp = '<option type="text" name="activityid" value="' + str(activity.activityid) + ' ">' + activity.activityname + '</option>'
            s = s+temp
    if change == True:
        s+='<option type="text" name="activityid" value="">-- Không có --</option>'
    data = {
        'is_taken': s,
    }

    return JsonResponse(data)


#lấy giá trị item được nhập vào để gán giá trị cho order
def validate_itemorderactivity(request):
    item = request.GET.get('item', None)
    ite = request.GET.get('ite', None)
    activitys = Activity.objects.filter(itemid=item)
    act = Activity.objects.get(activityid = request.GET.get('act', None))
    
    if len(activitys) == 0:
        s = 1
    else:
        listorder=[]
        if int(ite) == int(item):
            s = act.order
        else:
            for activity in activitys:
                listorder.append(activity.order) 
                
            s=max(listorder) + 1
    
    data = {
        'is_taken': s,
    }

    return JsonResponse(data)
