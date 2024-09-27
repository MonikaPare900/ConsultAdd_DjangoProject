from django.contrib import admin

from  . import models

# Register your models here.
#admin.register(models.UserDetails)
@admin.register(models.UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display=('username','email','password')
