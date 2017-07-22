from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess
from main.models import PbAvailablePlaforms,PbSubdomains
from account.models import User
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def create_all_playform(user):
    try:
        logger.info('Getting user detail')
        user = User.objects.get(pk=user)
        logger.info('Removing dots')
        username = user.username.replace(".","")
        logger.info('Executing script')
        subprocess.check_call(["sudo", "/home/ebuka/all_platform.sh", username])
        logger.info('Updating subdomains')
        # os.popen("sudo  %s" % ("/home/ebuka/wordpress.sh "+username+".playboard.xyz"+" "+username))
        for p in PbAvailablePlaforms.objects.all():
            PbSubdomains.object.create(
                owner=user,
                name=p.name,
                link="{0]-{1}.playboard.xyz".format(user,p.name)
            )
    except subprocess.CalledProcessError as e:
        logger.info('error occurred')
        logger.info(e.output)

    logger.info('Returning')


@shared_task
def create_wordpress(user):
    try:
        user = User.objects.get(pk=user)

        username = user.username.replace(".","")
        subprocess.check_call(["sudo", "/home/ebuka/wordpress.sh", username+"-wordpress",username])
    except subprocess.CalledProcessError:
        pass


@shared_task
def create_magento_2(user):
    try:
        user = User.objects.get(pk=user)
        username = user.username.replace(".","")
        subprocess.check_call(["sudo", "/home/ebuka/magento_2.sh", username+"-magento2",username])
    except subprocess.CalledProcessError:
        pass
