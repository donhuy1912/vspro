from django.shortcuts import render

# Create your views here.

def admin1 (request):
    return render(request, 'adminpage/admin1.html')

def admin2 (request):
    return render(request, 'adminpage/admin2.html')

