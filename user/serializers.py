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


class RegisterSerializer(serializers.Serializer):
    """
    회원가입 시리얼라이저
    """
    username = serializers.CharField(max_length=100, write_only=True)
    password1 = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(max_length=100, write_only=True)
    name = serializers.CharField(max_length=100, write_only=True)
    gender = serializers.ChoiceField(User.GenderChoices)

    def validate_username(self, username):
        """
        username의 입력 값 확인
        username의 중복 확이
        """
        if not username:
            raise serializers.ValidationError(
                _('username field not allowed empty')
            )

        # 대소문자를 구분하지 않기 위해 iexact를 사용
        get_user = User.objects.filter(username__iexact=username)

        if get_user.count() > 0:
            raise serializers.ValidationError(
                _('username is already registered')
            )
        return username

    def validate(self, data):
        """
        username 검증
        password 검증
        """
        data['username'] = self.validate_username(data['username'])
        # user/utils.py
        data['password1'] = validate_password12(data['password1'], data['password2'])
        return data

    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            password=validate_data['password1'],
            email=validate_data['email'],
            name=validate_data['name'],
            gender=validate_data['gender']
        )
        return user














