from django.urls import path   
from . import views

urlpatterns = [
path('addeducation/',views.addeducation),
path('addexperience/',views.addexperience),
path('createprofile/',views.createprofile),
path('dashboard/',views.dashboard),
path('login/',views.login),
path('profile/',views.profile),
path('profiles/',views.profiles),
path('register/',views.register),
]
