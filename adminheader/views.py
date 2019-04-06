from django.shortcuts import render, redirect
from homepage.models import Header
from datetime import datetime
from homepage.myfunction import tokenFile

# Create your views here.

def index(request):
    headers = Header.objects.all()
    for header in headers:
        header.createdate = header.createdate
        header.editdate = header.editdate
    context = {'headers': headers}
    return render(request, 'adminheader/header_show.html', context)

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
            
        header = Header( 
                                headername=request.POST['headername'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=request.POST['link'],
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        header.save()
        return redirect('/adminheader/')
    return render(request, 'adminheader/header_create.html')

def edit(request, id):
    header = Header.objects.get(headerid=id)
    header.createdate = header.createdate
    header.editdate = datetime.now()
    context = {'header': header}
    return render(request, 'adminheader/header_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    header = Header.objects.get(headerid=id)
    #Lấy url của image
    try:
        token_image = request.FILES['image']
    except:
        token_image = None
    ima = ''
    if token_image != None:
        ima = tokenFile(token_image)
    else:
        ima = header.image

    
    header.headername=request.POST['headername']
    header.createdate=header.createdate
    header.editdate=datetime.now()
    header.content=request.POST['content']
    header.link=request.POST['link']
    header.image=ima
    header.isenable=request.POST['isenable']
    header.note=request.POST['note']
    header.save()
    return redirect('/adminheader/')


def delete(request, id):
    header = Header.objects.get(headerid= id)
    header.delete()
    return redirect('/adminheader/')