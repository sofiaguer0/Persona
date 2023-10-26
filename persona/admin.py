from django.contrib import admin
from persona.models import persona

class PersonaAdmin(admin.ModelAdmin):
        list_display = ('apellido','nombre','dni','vive','id','email','created')
        list_filter=('vive','created')
        seach_fields=('dni','apellido')
        
        
admin.site.register(persona,PersonaAdmin)

