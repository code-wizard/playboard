from django.contrib import admin
from account import models
# Register your models here.


@admin.register(models.PbOngoingCreationTask)
class IbRunningTaskAdmin(admin.ModelAdmin):
    pass
