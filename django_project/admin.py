from django.contrib import admin
from django_project.models import Gifts


class UserAdmin(admin.ModelAdmin):
    list_display = ["email","username","password"]
class GiftsAdmin(admin.ModelAdmin):
    list_display = ["gift","username"]
admin.site.register(Gifts,GiftsAdmin)








