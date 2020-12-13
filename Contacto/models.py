from django.db import models
from django.core.validators import validate_email,validate_slug

# Create your models here.
class Cliente_Contacto (models.Model):
    name=models.CharField(validators=[validate_slug],max_length=50,verbose_name="Name")
    email=models.EmailField(validators=[validate_email],verbose_name="Email")
    
    class Meta:
        #db_table = 'Cliente'
        verbose_name = 'Cliente'

    def __str__(self):
        return "El Clientes es %s y su email es: %s"%(self.name,self.email)
    
 
    

class Cliente_message(models.Model):
    cliente=models.ForeignKey('Cliente_Contacto',on_delete=models.PROTECT)
    message=models.TextField(verbose_name="Message")
    subject=models.CharField(max_length=100,verbose_name="Subject")
    date=models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        #db_table = 'Mensaje'
        verbose_name = 'Mensaje'


    def __str__(self):
        return self.message
    
    