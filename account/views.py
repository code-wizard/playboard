from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import request
from main.models import PbSubdomains, PbConfig, PbAvailablePlaforms
from django.contrib.auth import login as django_login,authenticate,logout as django_logout
from django.contrib.auth.decorators import login_required
import subprocess
from account import tasks
from account.models import User
import os
# Create your views here.

#
# @login_required
# def my_playforms(request):
#
#     if not PbSubdomains.objects.filter(owner=request.user.id).exists():
#         ''''
#             This only execute once for each user
#         '''
#         platform = request.GET.get("platform")
#         if platform and not PbConfig.objects.filter(user=request.user.id, is_creating=True).exists():
#             user = User.objects.get(pk=request.user.id)
#             # username = user.username.replace(".", "")
#             create_all_playform.delay(user.id)
#         return render(request, "account/create_sub_domain.html")
#
#     else:
#         subdomains = PbSubdomains.objects.filter(owner=request.user.id)
#         context={
#             "subdomain": subdomains
#         }
#         return render(request, "account/my_platforms.html", context)


@login_required
def my_playforms(request):

        subdomains = PbSubdomains.objects.filter(owner=request.user.id)
        platforms = PbAvailablePlaforms.objects.all()
        context = {
            "subdomain": subdomains,
            "platform": platforms
        }
        return render(request, "account/my_platforms.html", context)


@login_required
def create_wordpress(request):
    platform = "Wordpress"
    if PbSubdomains.objects.filter(link__isnull=True, owner=request.user.id, name__icontains=platform).exists():
        ''''
            This only execute once for each user
        '''
        # platform = request.GET.get("platform")
        if platform and not PbConfig.objects.filter(user=request.user.id, is_creating=True, platform=platform).exists():
            user = User.objects.get(pk=request.user.id)
            # username = user.username.replace(".", "")
            tasks.create_wordpress.delay(user.id)
        return render(request, "account/create_sub_domain.html")

    else:
        subdomains = PbSubdomains.objects.filter(owner=request.user.id)
        context={
            "subdomain": subdomains
        }
        return render(request, "account/my_platforms.html", context)


@login_required
def save_platform_link(request):
    if request.POST:
        data = request.POST
        if data.get("link"):
            p = PbSubdomains.objects.get(owner=request.user.id, platform=data.get("platform"))
            p.link = data.get("link")
            p.save()
    return redirect("/account/my-platforms")
@login_required
def create_magento_2(request):
    platform = "Magento2"
    if not PbSubdomains.objects.filter(link__exact='', owner=request.user.id,  name__icontains=platform).exists():
        ''''
            This only execute once for each user
        '''
        if platform and not PbConfig.objects.filter(user=request.user.id, is_creating=True, platform=platform).exists():
            user = User.objects.get(pk=request.user.id)
            # username = user.username.replace(".", "")
            tasks.create_magento_2.delay(user.id)
        return render(request, "account/create_sub_domain.html")

    else:
        subdomains = PbSubdomains.objects.filter(owner=request.user.id)
        context={
            "subdomain": subdomains
        }
        return render(request, "account/my_platforms.html", context)


@login_required
def logout(request):
    django_logout(request)
    return redirect("/")

