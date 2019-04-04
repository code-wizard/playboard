from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess
from main.models import PbAvailablePlaforms,PbSubdomains,PbConfig
from account.models import User
from celery.utils.log import get_task_logger
from django.core.mail import send_mail


logger = get_task_logger(__name__)


@shared_task
def create_all_playform(user):
    try:
        if PbConfig.objects.filter(user=user).exists():
            config = PbConfig.objects.get(user=user)
            config.is_creating=True
            config.save()
        else:
            config = PbConfig.objects.create(
                user=User.objects.get(pk=user),
                is_creating=True
            )

        logger.info('Getting user detail')
        user = User.objects.get(pk=user)
        username = user.email.split('@')[0].rstrip('>')
        logger.info('Removing dots')
        username = username.replace(".", "")
        logger.info('Executing script for - '+username)
        for p in PbAvailablePlaforms.objects.all():
            PbSubdomains.objects.create(
                owner=user,
                name=p.name,
                link="{0}-{1}.playboard.xyz".format(username, p.name)
            )
        subprocess.check_call(["sudo", "/home/ebuka/playboard-setup/all_platform.sh", username])
        logger.info('Updating subdomains')
        # os.popen("sudo  %s" % ("/home/ebuka/wordpress.sh "+username+".playboard.xyz"+" "+username))
        
        body ="<p>Hello {0}</p>" \
              "<div>Your test environment is ready</div>"
        # send_mail(subject, message, from_email, to_list, fail_silently=True, html_message=html_message)
        logger.info('sending email')
        s=send_mail(
            'Playboard Test Environment',
            "Your test environment is ready",
            'achukwuebuka@regalix-inc.com',
            [user.email,"achukwuebuka@regalix-inc.com"],
            html_message = body.format(user.profile.first_name),
        )
        if s == 1:
            config.is_creating = False
            config.save()
            logger.info('Email was sent to '+user.email)
        else:
            config.is_creating = False
            config.save()
            logger.info('Unable to send email')

    except subprocess.CalledProcessError as e:
        logger.info('error occurred')
        logger.info(e.output)

    logger.info('Returning')


@shared_task
def create_wordpress(user):
    try:
        if PbConfig.objects.filter(user=user, platform='Wordpress').exists():
            config = PbConfig.objects.get(user=user)
            config.is_creating=True
            config.save()
        else:
            config = PbConfig.objects.create(
                user=User.objects.get(pk=user),
                is_creating=True,
                platform='Wordpress'
            )

        user = User.objects.get(pk=user)
        username = user.email.split('@')[0].rstrip('>')
        logger.info('Removing dots')
        username = username.replace(".", "")
        logger.info('Executing script for - ' + username)
        print("Agrument", username+"-wordpress", username)
        subprocess.check_call(["sudo", "/home/ebuka/playboard-setup/wordpress.sh", username+"-wordpress", username])
        sub = PbSubdomains.objects.get(
            owner=user,
            name="Wordpress",
        )
        sub.link = "{0}-{1}.playboard.xyz".format(username, "wordpress")
        sub.save()
        body = "<p>Hello {0}</p>" \
               "<div>Your Wordpress test environment is ready</div>"
        # send_mail(subject, message, from_email, to_list, fail_silently=True, html_message=html_message)
        logger.info('sending email')
        s = send_mail(
            'Playboard Test Environment',
            "Your test environment is ready",
            'achukwuebuka@regalix-inc.com',
            [user.email, "achukwuebuka@regalix-inc.com"],
            html_message=body.format(user.profile.first_name),
        )
        if s == 1:
            config.is_creating = False
            config.save()
            logger.info('Email was sent to ' + user.email)
        else:
            config.is_creating = False
            config.save()
            logger.info('Unable to send email')
    except subprocess.CalledProcessError:
        pass


@shared_task
def create_magento_2(user):
    try:
        if PbConfig.objects.filter(user=user, platform='Magento2').exists():
            config = PbConfig.objects.get(user=user)
            config.is_creating=True
            config.save()
        else:
            config = PbConfig.objects.create(
                user=User.objects.get(pk=user),
                is_creating=True,
                platform='Magento2'
            )
        user = User.objects.get(pk=user)
        username = user.email.split('@')[0].rstrip('>')
        logger.info('Removing dots')
        username = username.replace(".", "")
        logger.info('Executing script for - ' + username)
        print(username+"-magento2", username, "test")
        subprocess.check_call(["sudo", "/home/ebuka/playboard-setup/magento2.sh", username+"-magento2", username])

        sub = PbSubdomains.objects.get(
            owner=user,
            name="magento2",
        )
        sub.link = "{0}-{1}.playboard.xyz".format(username, "magento2")
        sub.save()

        body = "<p>Hello {0}</p>" \
               "<div>Your Magento2 test environment is ready</div>"
        logger.info('sending email')
        s = send_mail(
            'Playboard Test Environment',
            "Your test environment is ready",
            'achukwuebuka@regalix-inc.com',
            [user.email, "achukwuebuka@regalix-inc.com"],
            html_message=body.format(user.profile.first_name),
        )
        if s == 1:
            config.is_creating = False
            config.save()
            logger.info('Email was sent to ' + user.email)
        else:
            config.is_creating = False
            config.save()
            logger.info('Unable to send email')
    except subprocess.CalledProcessError:
        pass
