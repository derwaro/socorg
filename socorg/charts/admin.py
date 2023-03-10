from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Chart, Persona

admin.site.register(Chart)
admin.site.register(Persona)
