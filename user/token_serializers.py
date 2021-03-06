from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['gender'] = user.gender
        token['name'] = user.name
        token['is_staff'] = user.is_staff
        token['is_active'] = user.is_active

        return token


class APIRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass



