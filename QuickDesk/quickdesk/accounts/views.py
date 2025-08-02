# accounts/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializer import RegisterSerializer
from .models import CustomUser # Make sure to import your CustomUser model

# View for User Registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

# View for User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Create or get a token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        # If authentication fails, return an error
        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
