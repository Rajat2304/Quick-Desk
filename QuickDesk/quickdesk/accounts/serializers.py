# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # Define the fields to include in the registration request
        fields = ('username', 'email', 'password', 'role')
        # This option ensures the password is not sent back in the API response
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This method handles creating the user with a securely hashed password
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            role=validated_data.get('role', 'end_user')
        )
        return user
