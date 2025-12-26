from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        read_only_fields = ['id']

    def validate(self, data):
        if not data['password']:
            raise serializers.ValidationError({"password": "Passwords is empty"})
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        return User.objects.create_user(email=validated_data['email'], password=password)
