from django.shortcuts import render,redirect
from django.http import request
from main.models import PbSubdomains
from django.contrib.auth import login as django_login,authenticate,logout as django_logout
from django.contrib.auth.decorators import login_required
import subprocess
from account.tasks import create_all_playform
from account.models import User
# Create your views here.


def my_playforms(request):
    if not PbSubdomains.objects.filter(owner=request.user.id).exists():
        # try:
            user = User.objects.get(pk=request.user.id)
            username = user.username.replace(".", "")
            subprocess.check_call(["/home/ebuka/all_platform.sh", username])
            return render(request,"account/create_sub_domain.html")
        # except subprocess.CalledProcessError:
        #     pass


    else:
        context={}
        return render(request,"account/my_platforms.html",context)


@login_required
def logout(request):
    django_logout(request)
    return redirect("/")

