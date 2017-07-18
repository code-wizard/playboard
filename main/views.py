from django.shortcuts import render
from django.http import request

# Create your views here.


def index(request):

    return render(request,"main/index.html")


def create_sub_domain(request):
    return render(request, "main/create_sub_domain.html")
