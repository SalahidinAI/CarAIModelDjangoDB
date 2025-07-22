from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class PredictSerializer(serializers.Serializer):
    region = serializers.CharField(max_length=64)
    # price = serializers.IntegerField()
    year = serializers.IntegerField()
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    condition = serializers.CharField(max_length=64)
    cylinders = serializers.CharField(max_length=64)
    fuel = serializers.CharField(max_length=64)
    odometer = serializers.IntegerField()
    title_status = serializers.CharField(max_length=64)
    transmission = serializers.CharField(max_length=64)
    drive = serializers.CharField(max_length=64)
    type = serializers.CharField(max_length=64)
    paint_color = serializers.CharField(max_length=64)
    state = serializers.CharField(max_length=64)

