from django.shortcuts import render

# Create your views here.

def admin1 (request):
    return render(request, 'adminpage/admin1.html')

def admin2 (request):
    return render(request, 'adminpage/admin2.html')

# def tables_object (request):
#     return render(request, 'adminpage/tables_object.html')

# def tables_relationship (request):
#     return render(request, 'adminpage/tables_relationship.html')

# def tables_SEO (request):
#     return render(request, 'adminpage/tables_SEO.html')
