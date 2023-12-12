from django.contrib import admin
from django_project.models import Gifts, MyUser


class UserAdmin(admin.ModelAdmin):
    list_display = ["username","password"]

class GiftsAdmin(admin.ModelAdmin):
    list_display = ["gift","username"]
admin.site.register(Gifts,GiftsAdmin)
admin.site.register(MyUser, UserAdmin)








