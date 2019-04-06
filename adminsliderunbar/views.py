from django.shortcuts import render, redirect
from homepage.models import SlideRunBar
from datetime import datetime
from homepage.myfunction import tokenFile

# Create your views here.

def index(request):
    sliderunbars = SlideRunBar.objects.all()
    for sliderunbar in sliderunbars:
        sliderunbar.createdate = sliderunbar.createdate
        sliderunbar.editdate = sliderunbar.editdate
    context = {'sliderunbars': sliderunbars}
    return render(request, 'adminsliderunbar/sliderunbar_show.html', context)

def create(request):
    if request.method == 'POST':
        #Lấy url của image
        try:
            token_image = request.FILES['image']
        except:
            token_image = None
        ima = ''
        if token_image != None:
            ima = tokenFile(token_image)

        sliderunbar = SlideRunBar( 
                                sliderunbarname=request.POST['sliderunbarname'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=request.POST['link'],
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        sliderunbar.save()
        return redirect('/adminsliderunbar/')
    return render(request, 'adminsliderunbar/sliderunbar_create.html')

def edit(request, id):
    sliderunbar = SlideRunBar.objects.get(sliderunbarid=id)
    sliderunbar.createdate = sliderunbar.createdate
    sliderunbar.editdate = datetime.now()
    context = {'sliderunbar': sliderunbar}
    return render(request, 'adminsliderunbar/sliderunbar_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    sliderunbar = SlideRunBar.objects.get(sliderunbarid=id)
    #Lấy url của image
    try:
        token_image = request.FILES['image']
    except:
        token_image = None
    ima = ''
    if token_image != None:
        ima = tokenFile(token_image)
    else:
        ima = sliderunbar.image
    
    sliderunbar.sliderunbarrname=request.POST['sliderunbarname']
    sliderunbar.createdate=sliderunbar.createdate
    sliderunbar.editdate=datetime.now()
    sliderunbar.content=request.POST['content']
    sliderunbar.link=request.POST['link']
    sliderunbar.image=ima
    sliderunbar.isenable=request.POST['isenable']
    sliderunbar.note=request.POST['note']
    sliderunbar.save()
    return redirect('/adminsliderunbar/')


def delete(request, id):
    sliderunbar = SlideRunBar.objects.get(sliderunbarid= id)
    sliderunbar.delete()
    return redirect('/adminsliderunbar/')