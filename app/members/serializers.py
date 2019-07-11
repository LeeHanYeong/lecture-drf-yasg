from rest_framework import serializers

from .models import User

__all__ = (
    'UserSerializer',
    'UserCreateSerializer',
    'UserUpdateSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )
