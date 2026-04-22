from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.tokens import default_token_generator

class RegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    Handles POST requests to create a new user account. 
    Validates the input data and returns a success response if the registration is successful.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = default_token_generator.make_token(user)
        user = serializer.save()
        user.is_active = False
        user.save()

        return {
            'user': {
                'id': user.id,
                'email': user.email,
            },
            'token': token,
        }