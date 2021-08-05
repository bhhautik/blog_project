from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('register_user',views.register_user,name='register_user'),
    path('logout',views.logout,name='logout'),
    path('viewdetailes/<int:id>/',views.viewdetailes,name='viewdetailes'),
    path('moredetailes/<int:id>/',views.moredetailes,name='moredetailes'),
    path('create_post',views.create_post,name='create_post'),
]
