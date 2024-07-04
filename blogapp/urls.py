from django.urls import path
from django.contrib import admin
from . import views
from blogapp.views import *

urlpatterns = [
    # path('',views.home,name="index.html"),
    path('about/',about,name='about'),
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('dashbord/',dashbord,name='dashbord'),
    path('signup/',user_signup,name='user_signup'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='user_logout'),
    path('addpost/', add_post,name='addpost'),
    path('updatepost/<int:id>/',update_post,name='updatepost'),
    path('delete/<int:id>/',delete_post,name='deletepost'),   
]