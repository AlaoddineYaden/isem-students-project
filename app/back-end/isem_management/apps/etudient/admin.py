from django.contrib import admin
from .models import Departement, Etudient, Filiere, Matiere, Note, Module

class EtudientAdmin(admin.ModelAdmin):
    list_display = ('user', 'cne', 'cin', 'filiere')
    search_fields = ('user__first_name', 'user__last_name', 'cne', 'cin')
    list_filter = ('filiere',)

admin.site.register(Etudient, EtudientAdmin)
admin.site.register(Departement)
admin.site.register(Filiere)
admin.site.register(Matiere)
admin.site.register(Note)
admin.site.register(Module)
