from django.shortcuts import render, redirect
from userdetail.models import Item, Lesson, Account, Chapter, Subject
from datetime import datetime
from django.http import JsonResponse

# Create your views here.

def index(request):
    items = Item.objects.all()
    for item in items:
        item.createdate = item.createdate
        item.editdate = item.editdate
    context = {'items': items}
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    if request.method == 'POST':
        item = Item( 
                                accountid = Account.objects.get(accountid = request.POST['accountid']),
                                lessonid = Lesson.objects.get(lessonid = request.POST['lessonid']),
                                itemname=request.POST['itemid'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                description=request.POST['description'],
                                content=request.POST['content'],
                                order=request.POST['order'],
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        item.save()
        return redirect('/tables_object/')
    else:
        lessons = Lesson.objects.all()
        accounts = Account.objects.all()
        subjects = Subject.objects.all()
        
    
        for lesson in lessons:
            lesson.createdate = lesson.createdate
            lesson.editdate = lesson.editdate

        for account in accounts:
            account.createdate = account.createdate
            account.editdate = account.editdate

        for subject in subjects:
            subject.createdate = subject.createdate
            subject.editdate = subject.editdate
        context = {
            'lessons': lessons,
            'accounts': accounts,
            'subjects': subjects,
        }
    return render(request, 'item/item_create.html', context)

def edit(request, id):
    item = Item.objects.get(itemid=id)
    subjectid = item.lessonid.chapterid.subjectid

    item.createdate = item.createdate
    item.editdate = datetime.now()

    lessons = Lesson.objects.all()
    accounts = Account.objects.all()
    subjects = Subject.objects.all()
    for lesson in lessons:
        lesson.createdate = lesson.createdate
        lesson.editdate = lesson.editdate

    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate

    context = {
        'item': item,
        'lessons': lessons,
        'accounts': accounts,
        'subjects': subjects,
        'subjectid': subjectid,
    }
    return render(request, 'item/item_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    item = Item.objects.filter(itemid = id).update(accountid = Account.objects.get(accountid = getNum(request.POST['accountid'])))
    item = Item.objects.filter(itemid = id).update(lessonid = Lesson.objects.get(lessonid = getNum(request.POST['lessonid'])))
    item = Item.objects.get(itemid=id)
    item.itemname=request.POST['itemid']
    item.createdate=item.createdate
    item.editdate=datetime.now()
    item.description=request.POST['description']
    item.content=request.POST['content']
    item.order=request.POST['order']
    item.isenable=request.POST['isenable']
    item.note=request.POST['note']
    item.save()
    return redirect('/tables_object/')


def delete(request, id):
    item = Item.objects.get(itemid= id)
    item.delete()
    return redirect('/tables_object/')


#lấy giá trị subject được nhập vào để giới hạn giá trị show ra của chapter
def validate_subjectitem(request):
    subject = request.GET.get('subject', None)
    chapters = Chapter.objects.filter(subjectid=subject)
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True
        
    if edit == True:
        item  = Item.objects.get(itemid = request.GET.get('item', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="chapterid" value="">-- Chọn --</option>'
    else:
        if change == False:
            s= ' <option type="text" name="chapterid" value="' + str(item.lessonid.chapterid.chapterid) + ' ">' + item.lessonid.chapterid.chaptername + '</option>'
    
    temp = ''

    for chapter in chapters: 
        if edit == True and change == False:
            if chapter.chapterid!=item.lessonid.chapterid.chapterid:
                    temp = ' <option type="text" name="chapterid" value="' + str(chapter.chapterid) + ' ">' + chapter.chaptername + '</option>'
        else:
            temp = ' <option type="text" name="chapterid" value="' + str(chapter.chapterid) + ' ">' + chapter.chaptername + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)


#lấy giá trị chapter được nhập vào để giới hạn giá trị show ra của lesson
def validate_chapteritem(request):
    chapter = request.GET.get('chapter', None)
    
    lessons = Lesson.objects.filter(chapterid=chapter)
    
    edit = request.GET.get('edit', False)
    if edit == '1': 
        edit = True
    
    change = request.GET.get('change', False)
    if change == '1': 
        change = True

    if edit == True:
        item  = Item.objects.get(itemid = request.GET.get('item', None))
    
    if edit == False or change == True:
        s = '<option type="text" name="lessonid" value="">-- Chọn --</option>'
    else:
        s= ' <option type="text" name="lessonid" value="' + str(item.lessonid.lessonid) + ' ">' + item.lessonid.lessonname + '</option>'
    
    temp = ''

    for lesson in lessons: 
        if edit == True and change == False:
            if lesson.lessonid!=item.lessonid.lessonid:
                    temp = ' <option type="text" name="lessonid" value="' + str(lesson.lessonid) + ' ">' + lesson.lessonname + '</option>'
        else:
            temp = ' <option type="text" name="lessonid" value="' + str(lesson.lessonid) + ' ">' + lesson.lessonname + '</option>'
        s = s+temp

    data = {
        'is_taken': s
    }

    return JsonResponse(data)

def validate_lessonorderitem(request):
    lesson = request.GET.get('lesson', None)
    les = request.GET.get('les', None)
    items = Item.objects.filter(lessonid = lesson)
    ite = Item.objects.get(itemid = request.GET.get('ite', None))
   
    if len(items) == 0:
        s = 1
    else:
        listorder = []
        if int(lesson) == int(les):
            s = ite.order
        else:
            for item in items:
                listorder.append(item.order)
            s = max(listorder) + 1
    
    data = {
        'is_taken': s
    }
    return JsonResponse(data)