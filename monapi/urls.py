from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/new/', views.new_car, name='new_car'),
    path('car/<int:id>/', views.car_details, name='car_details'),
    path('car/', views.get_cars, name='getcars'),
]