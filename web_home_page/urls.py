from django.urls import path
from web_home_page import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('all_temperature', views.temperature_all_without_plot, name='temperature_all_without_plot')
]