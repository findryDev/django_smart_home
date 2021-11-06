from django.urls import path
from web_home_page import views

urlpatterns = [
    path('home', views.index, name='index')
]