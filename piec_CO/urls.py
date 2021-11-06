from django.urls import path
from piec_CO import views

urlpatterns = [
    path('piec_co/temperature_in/', views.temperature_in_list),
    path('piec_co/temperature_out/', views.temperature_out_list),
    path('piec_co/temperature_return/', views.temperature_return_list)
]