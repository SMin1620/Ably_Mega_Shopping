from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.utils import validate_password12
from user.token_serializers import MyTokenObtainPairSerializer


class LoginSerializer(serializers.ModelSerializer):
    """
    로그인 시리얼라이저
    """
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'password'
        ]

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if User.objects.filter(username=username).exists():
            get_user = User.objects.get(username=username)

            if not get_user.check_password(password):
                raise serializers.ValidationError(
                    _('Check Your Password')
                )
        else:
            raise serializers.ValidationError(
                _('User does not exist')
            )

        user = authenticate(username=username, password=password)
        token = MyTokenObtainPairSerializer.get_token(user)

        data = {
            'user': user.id,
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        }

        return data









