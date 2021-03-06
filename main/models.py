from django.db import models

# Create your models here.


class PbAvailablePlaforms(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table ="pb_avialable_platforms"


class PbSubdomains(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey("account.user",related_name="sub_domains", on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "pb_subdomains"


class PbConfig(models.Model):
    user = models.ForeignKey("account.user",related_name="user_config",on_delete=models.CASCADE)
    is_creating = models.BooleanField(default=False)


    class Meta:
        db_table = "pb_config"

