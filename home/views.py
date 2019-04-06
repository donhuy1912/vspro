from django.shortcuts import render, redirect
from userdetail.models import Home
from datetime import datetime
from homepage.myfunction import tokenFile
# Create your views here.

def index(request):
    homes = Home.objects.all()
    for home in homes:
        home.createdate = home.createdate
        home.editdate = home.editdate
    context = {'homes': homes}
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

        home = Home( 
                                homename=request.POST['homename'], 
                                createdate= datetime.now(), 
                                editdate= datetime.now(),
                                content=request.POST['content'],
                                link=lin,
                                image=ima,  
                                isenable=request.POST['isenable'],  
                                note=request.POST['note'])
        home.save()
        return redirect('/tables_SEO/')
    return render(request, 'home/home_create.html')

def edit(request, id):
    home = Home.objects.get(homeid=id)
    home.createdate = home.createdate
    home.editdate = datetime.now()
    context = {'home': home}
    return render(request, 'home/home_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def update(request, id):
    home = Home.objects.get(homeid=id)
    home.homename=request.POST['homename']
    home.createdate=home.createdate
    home.editdate=datetime.now()
    home.content=request.POST['content']
    home.link=request.POST['link']
    home.image=request.POST['image']
    home.isenable=request.POST['isenable']
    home.note=request.POST['note']
    home.save()
    return redirect('/tables_SEO/')


def delete(request, id):
    home = Home.objects.get(homeid= id)
    home.delete()
    return redirect('/tables_SEO/')