from django.db.models.signals import post_save
from django.dispatch import receiver
from account import models
from main.models import PbSubdomains, PbAvailablePlaforms


@receiver(post_save, sender=models.User)
def post_save_constant(sender, instance, created, **kwargs):
    if created:
        for sub in PbAvailablePlaforms.objects.all():
            PbSubdomains.objects.create(
                owner=instance,
                name=sub.name,
                platform=sub
            )
