from django.conf.urls import url
import account.views as av

urlpatterns =[
    url(r'my-platforms',av.my_playforms,name="my-platforms"),
    url(r'^logout/', av.logout, name="logout"),
]