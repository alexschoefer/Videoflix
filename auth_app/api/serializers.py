from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

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
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for obtaining JWT tokens using email and password.
    """

    def validate(self, attrs):
        """
        Validate the email and password, and generate JWT tokens if the credentials are valid.
        Args:
            attrs: A dictionary containing the email and password.
        Returns:
            A dictionary containing the refresh and access tokens, and the user object if authentication is successful.
        Raises:
            serializers.ValidationError: If the email or password is invalid, or if the account is not activated.
        """
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_active:
            raise serializers.ValidationError("Account is not activated.")

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user
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