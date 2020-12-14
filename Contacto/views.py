from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.template import Context

from django.template.loader import render_to_string 
from django.core.mail import EmailMessage

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

    

def envio_email(contx):

    """ Envio de template como string
        plaintext=get_template('Contacto/email.txt')
        text_content = plaintext.render(contx)
        send_mail(subject,text_content,email_from,recipient_list)"""


    htmly     = 'Contacto/email.html'
    html_message = render_to_string(htmly, contx)
    try:
        send_mail(contx['subject'],"",contx['email_from'],contx['recipient_list'],html_message=html_message)
        return 'Mensaje Enviado'
    except:
        return Exception('XYZ has gone wrong...')
        
    

    """ Esta funcion EmailMessage es otra opcion para enviar mensajes
        message_html = EmailMessage(subject, html_message, email_from, recipient_list)
        message_html.content_subtype = 'html' # this is required because there is no plain text email version
        message_html.send() """



def contactForm (request):
    ''' Utilizando la API FORMS de Django'''
    if request.method=="POST":
        #Guarda la informacion del formulario en variables.
        email_from=settings.EMAIL_HOST_USER # Desde donde se envian los mensajes
        recipient_list=[settings.EMAIL_HOST_RECIPIENT] #A donde llegan los mensajes enviados     

        formulario=ContactoForm(request.POST,auto_id='%s')

        if formulario.is_valid():
            
            info_formulario=formulario.cleaned_data

            subject=info_formulario['subject']
            email_client=info_formulario['email']
            name=info_formulario['name']
            message=info_formulario['message']
            
            contx={"name":name,"email_client":email_client,"subject":subject,"message":message,"email_from":email_from,"recipient_list":recipient_list}

            status_envio_email= envio_email(contx)






            #Limpia el formulario
            formulario=ContactoForm(auto_id='%s')
            
            #return HttpResponseRedirect('/contact')
            return render(request,'Contacto/contactForm.html',{"form":formulario,"envio":status_envio_email})

        # else:
            
        #     return render(request, 'Contacto/contactForm.html', context={'form': formulario})

            
    else:
        formulario=ContactoForm(auto_id='%s') # EL formulario Vacio
    return render(request,'Contacto/contactForm.html',{"form":formulario})


        
        
        

    
