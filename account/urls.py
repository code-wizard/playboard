from django.urls import path

import account.views as av

app_name = "account"

urlpatterns = [
    path('my-platforms',av.my_playforms, name="my-platforms"),
    path('logout/', av.logout, name="logout"),
]