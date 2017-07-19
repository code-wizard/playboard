from django.contrib import admin
from main.models import PbAvailablePlaforms,PbSubdomains
# Register your models here.


class AvailablePlatforms(admin.ModelAdmin):
    list_display = ("name","date_added")


class Subdomains(admin.ModelAdmin):
    list_display = ("name","owner","date_created")


admin.site.register(PbAvailablePlaforms,AvailablePlatforms)
admin.site.register(PbSubdomains,Subdomains)