from django.contrib import admin
from main.models import PbAvailablePlaforms,PbSubdomains,PbConfig
# Register your models here.


class AvailablePlatforms(admin.ModelAdmin):
    list_display = ("name","date_added")


class Subdomains(admin.ModelAdmin):
    list_display = ("name","owner","link","date_created")


class Config(admin.ModelAdmin):
    list_display = ("user","is_creating")
    
admin.site.register(PbAvailablePlaforms,AvailablePlatforms)
admin.site.register(PbConfig,Config)
admin.site.register(PbSubdomains,Subdomains)