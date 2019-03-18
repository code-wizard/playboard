from django.urls import path

import main.views as mv


app_name = "main"

urlpatterns = [
    path('create-sub-domain', mv.create_sub_domain, name="create-subdomain"),

]