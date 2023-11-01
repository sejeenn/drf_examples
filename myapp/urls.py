from django.urls import path
from .views import (
    get_random_number,                          # этот код из первой части
    UserRegistrationAPIView,
)

urlpatterns = [
    path('random-number/', get_random_number),  # этот код из первой части
    path('users/registration/',
         UserRegistrationAPIView.as_view(),
         name='user-register'),
]
