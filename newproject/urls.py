from django.contrib import admin
from django.urls import path, include
from authentication.urls import *
from authentication.views import login_view, register_user
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # path('', include('authentication.urls')),

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('', include('DasboardApp.urls')),

]