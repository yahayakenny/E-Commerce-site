from django.urls import path
from accounts_app.views import *
from accounts_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'account/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'account/logout.html'), name='logout'), 

]