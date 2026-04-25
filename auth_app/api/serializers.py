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
        Validate the email and password, and return the token if valid.
        """
        email = attrs.get('email')
        password = attrs.get('password')

        try: 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")
        
        data = super().validate(attrs)
        
        return data


