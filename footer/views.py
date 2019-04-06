from django.shortcuts import render, redirect
from userdetail.models import Footer
from datetime import datetime
from homepage.myfunction import tokenFile

# Create your views here.

def index(request):
    footers = Footer.objects.all()
    for footer in footers:
        footer.createdate = footer.createdate
        footer.editdate = footer.editdate
    context = {'footers': footers}
    return render(request, 'adminpage/tables_SEO.html', context)

def create(request):
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
    
    if request.method == 'POST':
        footer = Footer( 
                                footername=request.POST['footername'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=lin,
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        footer.save()
        return redirect('/tables_SEO/')
    return render(request, 'footer/footer_create.html')

def edit(request, id):
    footer = Footer.objects.get(footerid=id)
    footer.createdate = footer.createdate
    footer.editdate = datetime.now()
    context = {'footer': footer}
    return render(request, 'footer/footer_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    footer = Footer.objects.get(footerid=id)
    footer.footername=request.POST['footername']
    footer.createdate=footer.createdate
    footer.editdate=datetime.now()
    footer.content=request.POST['content']
    footer.link=request.POST['link']
    footer.image=request.POST['image']
    footer.isenable=request.POST['isenable']
    footer.note=request.POST['note']
    footer.save()
    return redirect('/tables_SEO/')


def delete(request, id):
    footer = Footer.objects.get(footerid= id)
    footer.delete()
    return redirect('/tables_SEO/')