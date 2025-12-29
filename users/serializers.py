from rest_framework import serializers
from django.contrib.auth import get_user_model

from profiles.serializers import ProfileSerializer
from profiles.models import Profile


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer() # Profile is being created itself

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'profile']
        read_only_fields = ['id']

    def validate(self, data):
        if not data['password']:
            raise serializers.ValidationError({"password": "Passwords is empty"})
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)

        password = validated_data.pop('password', None)

        # Create the user
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password
        )

        if profile_data:
            Profile.objects.create(user=user, **profile_data)

        return user
