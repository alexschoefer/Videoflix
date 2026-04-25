from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User

class RegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    Handles POST requests to create a new user account. 
    Validates the input data and returns a success response if the registration is successful.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.
        Validates the input data using the RegistrationSerializer, creates a new user, generates an activation token, and returns a response with the user information and token.
        Args:
            request: The incoming HTTP request object containing the registration data.
        Returns:
            A Response object containing the user information and activation token if registration is successful, or an error response if validation fails.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        return Response({
            'user': {
                'id': user.id,
                'email': user.email,
            },
            'token': token,
        }, status=status.HTTP_201_CREATED)
    
class AccountActivationView(APIView):
    """
    API view for account activation.
    Handles GET requests to activate a user account using an activation token. Validates the token and activates the account if the token is valid.
    """
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        """
        Handle GET requests for account activation.
        Validates the activation token and activates the user account if the token is valid.
        Args:
            request: The incoming HTTP request object.
            uidb64: The base64-encoded user ID extracted from the URL.
            token: The activation token extracted from the URL.
        Returns:
            A Response object indicating whether the account activation was successful or if the token is invalid.
        """
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)