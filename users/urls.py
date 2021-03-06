from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name='users'

urlpatterns=[
    path('profile/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/',views.register,name='register'),

]