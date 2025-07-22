from django.urls import path
from .views import *


urlpatterns = [
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('car/', CarListAPIView.as_view(), name='car_list'),
    path('predict/', Predict.as_view(), name='predict_car_price'),
]
