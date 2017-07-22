from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess
from main.models import PbAvailablePlaforms,PbSubdomains
from account.models import User
from celery.utils.log import get_task_logger
from django.core.mail import send_mail



logger = get_task_logger(__name__)


@shared_task
def create_all_playform(user):
    try:
        logger.info('Getting user detail')
        user = User.objects.get(pk=user)
        logger.info('Removing dots')
        username = user.username.replace(".","")
        logger.info('Executing script for - '+username)
        subprocess.check_call(["sudo", "/home/ebuka/all_platform.sh", username])
        logger.info('Updating subdomains')
        # os.popen("sudo  %s" % ("/home/ebuka/wordpress.sh "+username+".playboard.xyz"+" "+username))
        for p in PbAvailablePlaforms.objects.all():
            PbSubdomains.objects.create(
                owner=user,
                name=p.name,
                link="{0}-{1}.playboard.xyz".format(username,p.name)
            )
        body ="<p>Hello {0}</p>" \
              "<div>Your test environment is ready</div>"
        # send_mail(subject, message, from_email, to_list, fail_silently=True, html_message=html_message)

        send_mail(
            subject='Your test environment is ready',
            message="You test environment is ready",
            from_email='achukwuebuka@regalix-inc.com',
            html_message = body.format(user.profile.first_name),
            recipient_list=[user.email],
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
