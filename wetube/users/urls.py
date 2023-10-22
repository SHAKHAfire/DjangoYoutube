from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',all_users),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]