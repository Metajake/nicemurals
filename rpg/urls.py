from django.urls import path

from . import views

urlpatterns = [
    path('', views.rpgHome, name="rpg-home"),
    path('gainexperience', views.gainExperience, name="gain-experience"),
]
