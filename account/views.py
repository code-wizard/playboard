from django.shortcuts import render,redirect
from django.http import request
from main.models import PbSubdomains
from django.contrib.auth import login as django_login,authenticate,logout as django_logout
from django.contrib.auth.decorators import login_required
import subprocess
from account.tasks import create_all_playform
from account.models import User
import os
# Create your views here.


def my_playforms(request):
    if not PbSubdomains.objects.filter(owner=request.user.id).exists():
        try:
            user = User.objects.get(pk=request.user.id)
            username = user.username.replace(".", "")
            # subprocess.check_call(["sudo","su", "ebuka" ,"-c","/home/ebuka/test.sh", username+".playboard.xyz",username])
            # subprocess.check_call(["sudo","/home/ebuka/test.sh", username+".playboard.xyz",username])
            p = subprocess.Popen(['sudo', '-S',"/home/ebuka/test.sh", username+".playboard.xyz",username],
                                 stdin=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
            out,err= p.communicate("alexander" + '\n')[1]
            print(out,err)
            os.popen("sudo -S %s" % ("/home/ebuka/test.s", username+".playboard.xyz"+" "+username), 'w').write('alexander\n')

            return render(request,"account/create_sub_domain.html")
        except subprocess.CalledProcessError as e:
            print(e.output)
            # return render(request, "account/my_platforms.html", {"e":e})


    else:
        context={}
        return render(request,"account/my_platforms.html",context)


@login_required
def logout(request):
    django_logout(request)
    return redirect("/")

