from django.urls import path
from .views import get_random_number

urlpatterns = [
    path(
        'random-number/min_num/<int:min>/max_num/<int:max>/',
        get_random_number,

    ),
]
