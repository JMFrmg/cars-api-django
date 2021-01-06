
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('carsapi/', include('monapi.urls')),
    path('admin/', admin.site.urls),
]
