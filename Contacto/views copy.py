from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

from Contacto.models import *
from Contacto.forms import  ContactoForm

# Create your views here.
def contact (request):
    # now=datetime.now()
    if request.method=="POST":
        subject=request.POST["subject"]
        email_client=request.POST["email"]
        message=request.POST['message']+ " " + email_client
        name=request.POST["name"]
        email_from=settings.EMAIL_HOST_USER # Desde donde se envian los mensajes
        recipient_list=settings.EMAIL_HOST_RECIPIENT #A donde llegan los mensajes enviados

        #envio del email
        send_mail(subject,message,email_from,recipient_list)

        #guardar en BD.
        # Este hace un QuerySet, pero no crea el objeto
        Cliente=Cliente_Contacto.objects.filter(email=email_client)
        

        if Cliente:
            # existe


            # Cuando el email ya existe no valida el nombre
            # Modificar esta validacion

            Cliente=Cliente_Contacto.objects.get(email=email_client)
            m=Cliente_message(message=message,subject=subject,cliente=Cliente)
            m.save()        
        else:
            #No existe
            c=Cliente_Contacto(name=name,email=email_client)
            c.save()
            m=Cliente_message(message=message,subject=subject,cliente=c)
            m.save()
    return render(request,'Contacto/contact.html')

    


def contactForm (request):
    ''' Utilizando la API FORMS de Django'''
    if request.method=="POST":
        #Guarda la informacion del formulario en variables.
        subject=request.POST["subject"]
        email_client=request.POST["email"]
        message=request.POST['message']+ " " + email_client
        name=request.POST["name"]
        email_from=settings.EMAIL_HOST_USER # Desde donde se envian los mensajes
        recipient_list=settings.EMAIL_HOST_RECIPIENT #A donde llegan los mensajes enviados
        formulario=ContactoForm(request.POST)
        if formulario.is_valid():
            info_formulario=formulario.cleaned_data

            send_mail(info_formulario[subject],info_formulario[message],email_from,recipient_list)
            return HttpResponseRedirect('Contacto/contactForm.html')

            
        else:
            formulario=ContactoForm()
        return render(request,'Contacto/contactForm.html',{"form":formulario})


        
        
        

    
