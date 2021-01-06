from django import forms
from django.forms import ModelForm
from .models import Car, Brand, CustomerService

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["brand", "car_model", "puissance", "weight", "price", "door"]