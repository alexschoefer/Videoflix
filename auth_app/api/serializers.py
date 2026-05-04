from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.Serializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True)
    confirmed_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        """
        Check if the email is already in use.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def validate(self, data):
        """
        Check if the password and confirmed password match.
        """
        password = data.get('password')
        confirmed_password = data.get('confirmed_password')

        if password != confirmed_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        """
        Create a new user with the validated data.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['email'],
            is_active=False
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login using email and password.
    Returns JWT tokens if authentication is successful.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # 🔑 Wichtig: username=email (weil Django das erwartet)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_active:
            raise serializers.ValidationError("Account is not activated.")

        # JWT Tokens erzeugen
        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class PasswortResetSerializer(serializers.Serializer):
    """
    Serializer for password reset requests.
    """

    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        """
        Check if the email exists in the system.
        """
        if not User.objects.filter(email=value, is_active = True).exists():
            raise serializers.ValidationError("No user is associated with this email.")
        return value
    
class PasswordConfirmResetSerializer(serializers.Serializer):
    """
    Serializer for confirming password reset.
    """

    new_password = serializers.CharField(write_only=True)
    confirmed_password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Check if the new password and confirmed password match.
        """
        new_password = data.get('new_password')
        confirmed_password = data.get('confirmed_password')

        if new_password != confirmed_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data