from django.contrib import admin

from apps.professeur.models import Enseigner, Professeur

# Register your models here.
admin.site.register(Professeur)
admin.site.register(Enseigner)