from django.urls import path

from .views import aggregate_data

# URL-маршрути додатку aggregator.
urlpatterns = [
    path('aggregate/', aggregate_data, name='aggregate-data'),
]
