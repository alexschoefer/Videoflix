from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegistrationView, AccountActivationView, CookieTokenObtainPairView, LogoutView, TokenRefreshView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/activate/<uidb64>/<token>/', AccountActivationView.as_view(), name='activate'),
    path('api/login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm')
]

