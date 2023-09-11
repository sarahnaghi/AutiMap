from django.contrib import admin
from .models import SpecialistProfile

# Register your models here.

class SpecialistProfileAdmin(admin.ModelAdmin):
 list_display = ("major","user","city")

admin.site.register(SpecialistProfile, SpecialistProfileAdmin)