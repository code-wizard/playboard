from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess
from main.models import PbAvailablePlaforms,PbSubdomains
from account.models import User


@shared_task
def create_all_playform(user):
    try:
        user = User.objects.get(pk=user)
        # for p in platforms:
        username = user.username.replace(".","")
        subprocess.check_call(["",username])
    except subprocess.CalledProcessError:
        pass


@shared_task
def create_wordpress(user):
    return 1


@shared_task
def create_magento(user):
    return 1
