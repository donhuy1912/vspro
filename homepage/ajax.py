from django.shortcuts import render, redirect
from django.contrib import messages
from homepage.models import *
from homepage.myfunction import *
from django.core.mail import send_mail
from homepage.myclass import *
from django.http import JsonResponse
from datetime import datetime
 
def ajaxsentmes(request):
    
    data={
         's':True
    }
    return JsonResponse(data)