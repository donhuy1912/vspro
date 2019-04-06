from django.shortcuts import render, redirect
from homepage.models import Footer
from datetime import datetime
from homepage.myfunction import tokenFile

# Create your views here.

def index(request):
    footers = Footer.objects.all()
    for footer in footers:
        footer.createdate = footer.createdate
        footer.editdate = footer.editdate
    context = {'footers': footers}
    return render(request, 'adminfooter/footer_show.html', context)

def create(request):        
    #Lấy url của image
    try:
        token_image = request.FILES['image']
    except:
        token_image = None
    ima = ''
    if token_image != None:
        ima = tokenFile(token_image)
    
    if request.method == 'POST':
        footer = Footer( 
                                footername=request.POST['footername'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=request.POST['link'],
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        footer.save()
        return redirect('/adminfooter/')
    return render(request, 'adminfooter/footer_create.html')

def edit(request, id):
    footer = Footer.objects.get(footerid=id)
    footer.createdate = footer.createdate
    footer.editdate = datetime.now()
    context = {'footer': footer}
    return render(request, 'adminfooter/footer_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    footer = Footer.objects.get(footerid=id)
    #Lấy url của image
    try:
        token_image = request.FILES['image']
    except:
        token_image = None
    ima = ''
    if token_image != None:
        ima = tokenFile(token_image)
    else:
        ima = footer.image

    footer.footername=request.POST['footername']
    footer.createdate=footer.createdate
    footer.editdate=datetime.now()
    footer.content=request.POST['content']
    footer.link=request.POST['link']
    footer.image=ima
    footer.isenable=request.POST['isenable']
    footer.note=request.POST['note']
    footer.save()
    return redirect('/adminfooter/')


def delete(request, id):
    footer = Footer.objects.get(footerid= id)
    footer.delete()
    return redirect('/adminfooter/')