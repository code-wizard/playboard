from django.db import models

# Create your models here.


class PbSubdomains(models.Model):
    name = models.CharField(max_length=20,unique=True)
    owner = models.ForeignKey("account.user",related_name="sub_domains", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "pb_subdomains"

