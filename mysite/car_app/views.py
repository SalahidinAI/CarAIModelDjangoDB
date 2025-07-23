from rest_framework import generics, views, status
from .models import *
from .serializers import *
import joblib
from django.conf import settings
import os
from rest_framework.response import Response


regions = [
    'chattanooga', 'clarksville', 'franklin', 'gallatin',
    'henderson', 'knoxville', 'memphis', 'murfree', 'nashville'
]

manufacturers = [
    'audi', 'bmw', 'buick', 'cadillac', 'ford', 'honda', 'hyundai',
    'infiniti', 'jeep', 'kia', 'lincoln', 'mazda', 'nissan', 'toyota'
]

models = [
    'altima', 'cherokee', 'corolla', 'cx5', 'elantra', 'enclave avenir sport',
    'escalade esv', 'focus', 'ilx premium pkg', 'navigator l select',
    'q60 red sport', 'q8 premium', 'soul', 'x5'
]

conditions = [
    'fair', 'good', 'like new', 'salvage'
]

cylinders = [
    '3 cylinders', '4 cylinders', '5 cylinders', '6 cylinders', '8 cylinders'
]

fuels = [
    'electric', 'gas', 'hybrid', 'other'
]

title_status = [
    'lien', 'missing', 'rebuilt', 'salvage'
]

transmissions = [
    'cvt', 'manual', 'other'
]

drives = [
    'awd', 'fwd', 'other', 'rwd'
]

types = [
    'convertible', 'coupe', 'hatchback', 'other', 'pickup', 'sedan', 'van', 'wagon'
]

paint_colors = [
    'blue', 'gray', 'green', 'orange', 'purple', 'red', 'silver', 'white', 'yellow'
]

states = [
    'ar', 'ga', 'ky', 'ms', 'tn'
]


model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'scaler.pkl')
scaler = joblib.load(scaler_path)


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class Predict(views.APIView):
    def post(self, request):
        serializers = PredictSerializer(data=request.data)
        if serializers.is_valid():
            data = serializers.validated_data
            new_region = data.get('region')
            new_manufacturer = data.get('manufacturer')
            new_model = data.get('model')
            new_condition = data.get('condition')
            new_cylinders = data.get('cylinders')
            new_fuel = data.get('fuel')
            new_title_status = data.get('title_status')
            new_transmission = data.get('transmission')
            new_drive = data.get('drive')
            new_type = data.get('type')
            new_paint_color = data.get('paint_color')
            new_state = data.get('state')

            region_0_1 = [1 if i == new_region else 0 for i in regions]
            manufacturers_0_1 = [1 if i == new_manufacturer else 0 for i in manufacturers]
            model_0_1 = [1 if i == new_model else 0 for i in models]
            condition_0_1 = [1 if i == new_condition else 0 for i in conditions]
            cylinders_0_1 = [1 if i == new_cylinders else 0 for i in cylinders]
            fuel_0_1 = [1 if i == new_fuel else 0 for i in fuels]
            title_status_0_1 = [1 if i == new_title_status else 0 for i in title_status]
            transmission_0_1 = [1 if i == new_transmission else 0 for i in transmissions]
            drive_0_1 = [1 if i == new_drive else 0 for i in drives]
            type_0_1 = [1 if i == new_type else 0 for i in types]
            paint_color_0_1 = [1 if i == new_paint_color else 0 for i in paint_colors]
            state_0_1 = [1 if i == new_state else 0 for i in states]

            data_values = []
            for i in data:
                elem = data[i]
                if type(elem) != str:
                    data_values.append(elem)

            features = data_values + region_0_1 + manufacturers_0_1 + model_0_1 + condition_0_1 + cylinders_0_1 + fuel_0_1 + title_status_0_1 + transmission_0_1 + drive_0_1 + type_0_1 + paint_color_0_1 + state_0_1
            scaled_data = scaler.transform([features])
            prediction = model.predict(scaled_data)[0]
            car = serializers.save(price=prediction)

            return Response({'Prediction': round(prediction),
                             'data': PredictSerializer(car).data}, status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
