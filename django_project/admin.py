from django.contrib import admin
from django_project.models import Region, Input

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Region, RegionAdmin)
admin.site.register(Input)





