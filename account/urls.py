from django.urls import path

import account.views as av

app_name = "account"

urlpatterns = [
    path('my-platforms',av.my_playforms, name="my-platforms"),
    path('save-platform-link/',av.save_platform_link, name="save-link"),
    path('install/wordpress/',av.create_wordpress, name="wordpress"),
    path('install/magento2/',av.create_magento_2, name="magento2"),
    path('logout/', av.logout, name="logout"),
]