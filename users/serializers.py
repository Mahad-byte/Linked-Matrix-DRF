from django.contrib.auth import get_user_model
from rest_framework import serializers

from profiles.models import Profile
from profiles.serializers import ProfileSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "created_at"]
        read_only_fields = ["created_at"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)  # make nested profile optional

    class Meta:
        model = User
        fields = ["id", "email", "password", "profile"]
        read_only_fields = []

    def validate(self, data):
        if not data["password"]:
            raise serializers.ValidationError({"password": "Passwords is empty"})
        return data

    def create(self, validated_data):
        print(f"Validated data: {validated_data}")
        profile_data = validated_data.pop("profile", None)

        password = validated_data.pop("password", None)
        print("Creating User....")
        # Create the user
        user = User.objects.create_user(
            email=validated_data["email"], password=password
        )
        print("After creating User....")

        print("Creating Profile...")
        print("profile data: ", profile_data)
        if profile_data:
            profile = Profile.objects.create(user=user, **profile_data)
            print("created profile? ", profile)

        return {"id": user.id, "email": user.email, "profile": profile_data}
