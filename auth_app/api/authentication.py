from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        """
        Override the default authenticate method to retrieve the JWT token from cookies instead of the Authorization header.
        This method checks for the presence of the 'access_token' cookie, validates the token, and returns the associated user and token if valid.        
        Args:
            request: The incoming HTTP request object.
        Returns:
            A tuple of (user, token) if authentication is successful, or None if authentication fails.
        """
        access_token = request.COOKIES.get('access_token')

        if access_token is None:
            return None
        validated_token = self.get_validated_token(access_token)
        return self.get_user(validated_token), validated_token