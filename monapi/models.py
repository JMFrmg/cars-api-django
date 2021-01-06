from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Marque %s" % self.name


class CustomerService(models.Model):
    email = models.CharField(max_length=200)
    tel = models.IntegerField(default=0)


class Car(models.Model):
    brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    puissance = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    door = models.IntegerField(default=0)

    def __str__(self):
        return "Marque :" % self.brand

