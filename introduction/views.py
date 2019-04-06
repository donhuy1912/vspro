from django.shortcuts import render, redirect
from userdetail.models import *
from datetime import datetime
from homepage.myfunction import tokenFile
# Create your views here.

def index(request):
    introductions = Introduction.objects.all()
    headers = Header.objects.all()
    footers = Footer.objects.all()
    homes = Home.objects.all()
    sliderunbars = SlideRunBar.objects.all()

    for introduction in introductions:
        introduction.createdate = introduction.createdate
        introduction.editdate = introduction.editdate

    for header in headers:
        header.createdate = header.createdate
        header.editdate = header.editdate

    for footer in footers:
        footer.createdate = footer.createdate
        footer.editdate = footer.editdate

    for home in homes:
        home.createdate = home.createdate
        home.editdate = home.editdate

    for sliderunbar in sliderunbars:
        sliderunbar.createdate = sliderunbar.createdate
        sliderunbar.editdate = sliderunbar.editdate

    context = {'introductions': introductions,
                'headers': headers,
                'footers': footers,
                'homes': homes,
                'sliderunbars': sliderunbars}

    return render(request, 'adminpage/tables_SEO.html', context)

def create(request):
    if request.method == 'POST':
        # Lấy url của link
        try:
            token_link = request.FILES['link']
        except:
            token_link = None
        lin = ''
        if token_link != None:
            lin = tokenFile(token_link)

        # Lấy url của image
        try:
            token_image = request.FILES['image']
        except:
            token_image = None
        ima = ''
        if token_image != None:
            ima = tokenFile(token_image)

        introduction = Introduction( 
                                introductionname=request.POST['introductionname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=lin,
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        introduction.save()
        return redirect('/tables_SEO/')
    return render(request, 'introduction/introduction_create.html')

def edit(request, id):
    introduction = Introduction.objects.get(introductionid=id)
    introduction.createdate = introduction.createdate
    introduction.editdate = datetime.now()
    context = {'introduction': introduction}
    return render(request, 'introduction/introduction_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    introduction = Introduction.objects.get(introductionid=id)
    introduction.introductionname=request.POST['introductionname']
    introduction.createdate=introduction.createdate
    introduction.editdate=datetime.now()
    introduction.content=request.POST['content']
    introduction.link=request.POST['link']
    introduction.avatar=request.POST['image']
    introduction.isenable=request.POST['isenable']
    introduction.note=request.POST['note']
    introduction.save()
    return redirect('/tables_SEO/')


def delete(request, id):
    introduction = Introduction.objects.get(introductionid= id)
    introduction.delete()
    return redirect('/tables_SEO/')