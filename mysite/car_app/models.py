from django.db import models


class Car(models.Model):
    region = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField()
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    condition = models.CharField(max_length=64)
    cylinders = models.CharField(max_length=64)
    fuel = models.CharField(max_length=64)
    odometer = models.PositiveSmallIntegerField()
    title_status = models.CharField(max_length=64)
    transmission = models.CharField(max_length=64)
    drive = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    paint_color = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.manufacturer}'
