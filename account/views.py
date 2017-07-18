from django.shortcuts import render,redirect
from django.http import request
from main.models import PbSubdomains
from django.contrib.auth import login as django_login,authenticate,logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def my_playforms(request):
    if PbSubdomains.objects.filter(owner=request.user.id).exists():
        return redirect("create-sub-domain")
    else:
        context={}
        return render(request,"account/my_platforms.html",context)


@login_required
def logout(request):
    django_logout(request)
    return redirect("/")

