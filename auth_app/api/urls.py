from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegistrationView, AccountActivationView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/activate/<uidb64>/<token>/', AccountActivationView.as_view(), name='activate'),
]

