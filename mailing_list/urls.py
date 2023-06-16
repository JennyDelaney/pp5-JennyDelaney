from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailing_list, name='mailing_list'),
]