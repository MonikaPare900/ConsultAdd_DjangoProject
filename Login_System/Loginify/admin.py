from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.UserDetails)
@admin.register(models.UserDetails)
class Userdetails(admin.ModelAdmin):
    List_display = ('username','email','password') 