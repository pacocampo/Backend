from django.contrib import admin

from . import models
# Register your models here.

#admin.site.register(models.MyUser)
@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
	list_display = ['user']