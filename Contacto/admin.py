from django.contrib import admin

# Register your models here.
from Contacto.models import *

class ClienteAdmin(admin.ModelAdmin):
    """ Esta clase me permite mostrar los campos que yo quiero en el 
    panel de administracion.
        Recordando que hay que incluirlo en el:
        admin.site.register(Cliente_Contacto,ClienteAdmin)
        """

    list_display=("name","email")
    list_display_links = ["name","email"] #los muestra como links
   
    
class MessageAdmin(admin.ModelAdmin):
    list_display=("date","subject")
    list_filter=['date']
    search_fields=['subject','message']
    date_hierarchy = 'date'

    
    


class Cliente_message_Inline(admin.TabularInline):
    model = Cliente_message

class Cliente_ContactoAdmin(admin.ModelAdmin):
    inlines = (Cliente_message_Inline, )

admin.site.register(Cliente_Contacto,ClienteAdmin)
admin.site.register(Cliente_message,MessageAdmin)


# admin.site.register(Album)
# admin.site.register(Artist)
# admin.site.register(Customer)
# admin.site.register(Employee)
# admin.site.register(Genre)
# admin.site.register(Invoice)
# admin.site.register(Invoiceline)
# admin.site.register(Mediatype)
# admin.site.register(Playlist, PlaylistAdmin)
# admin.site.register(Track)