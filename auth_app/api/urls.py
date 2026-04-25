from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegistrationView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name='register'),
]

