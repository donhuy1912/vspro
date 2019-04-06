from django.shortcuts import render, redirect
from userdetail.models import Header
from datetime import datetime
from homepage.myfunction import tokenFile

# Create your views here.

def index(request):
    headers = Header.objects.all()
    for header in headers:
        header.createdate = header.createdate
        header.editdate = header.editdate
    context = {'headers': headers}
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
                                link=lin,
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        header.save()
        return redirect('/tables_SEO/')
    return render(request, 'header/header_create.html')

def edit(request, id):
    header = Header.objects.get(headerid=id)
    header.createdate = header.createdate
    header.editdate = datetime.now()
    context = {'header': header}
    return render(request, 'header/header_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    header = Header.objects.get(headerid=id)
    header.headername=request.POST['headername']
    header.createdate=header.createdate
    header.editdate=datetime.now()
    header.content=request.POST['content']
    header.link=request.POST['link']
    header.image=request.POST['image']
    header.isenable=request.POST['isenable']
    header.note=request.POST['note']
    header.save()
    return redirect('/tables_SEO/')


def delete(request, id):
    header = Header.objects.get(headerid= id)
    header.delete()
    return redirect('/tables_SEO/')