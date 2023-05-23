from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static                      # used for static files
from django.conf import settings
from django.contrib.auth.views import LogoutView
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    
    path('', include('homepage.urls')),

    # path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout"),

    path('inventory/', include('inventory.urls')),
    path('transactions/', include('transactions.urls')),
]