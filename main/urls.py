from django.conf.urls import url
import main.views as mv



urlpatterns =[
    url(r'create-sub-domain',mv.create_sub_domain,name="create-subdomain"),

]