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


class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
