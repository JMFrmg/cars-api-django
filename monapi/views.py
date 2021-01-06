from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Car, Brand, CustomerService
from .forms import CarForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_cars(request):
    cars = Car.objects.all()
    data = list(cars.values())

    return JsonResponse(data, safe=False)

def car_details(request, id):
    car = Car.objects.filter(pk=id)
    data = list(car.values())

    return JsonResponse(data[0], safe=False)

def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/carsapi/car/')

    else:
        form = CarForm()

    return render(request, "monapi/carform.html", locals())
