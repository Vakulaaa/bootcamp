from django.urls import path

from .views import decisions_aggregate, decisions_list

# URL-маршрути додатку local_government.
urlpatterns = [
    path('decisions/', decisions_list, name='lg-decisions-list'),
    path('decisions/aggregate/', decisions_aggregate, name='lg-decisions-aggregate'),
]
