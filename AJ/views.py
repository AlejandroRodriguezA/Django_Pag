from django.shortcuts import render

# Importaciones para el envio de mail en contacto
from django.core.mail import send_mail
from django.conf import settings
from . import views

# fin importaciones de email

# Create your views here.


def home (request):

    return render(request,'AJ/home.html')

def about (request):

    return render(request,'AJ/about.html')

def resume (request):

    return render(request,'AJ/resume.html')

def services (request):

    return render(request,'AJ/services.html')

def portfolio (request):

    return render(request,'AJ/portfolio.html')




def LogIn (reguest):
    
    return render(reguest,'AJ/LogIn.html')
