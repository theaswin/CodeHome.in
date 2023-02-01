from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name = 'HomePage'),
    path('VideoPage',views.VideoPage,name ='VideoPage'),
    path('LoginPage',views.LoginPage,name='LoginPage'),
]
