# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    TYPE_CHOICES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]
    type = models.CharField(default="SUV", choices=TYPE_CHOICES, max_length=25)
    year = models.IntegerField(
        default=2024, validators=[MaxValueValidator(2024), MinValueValidator(2015)]
    )

    def __str__(self):
        return self.name
