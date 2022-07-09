from django.http import HttpRequest
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User
from user.serializers import LoginSerializer
from user.token_serializers import MyTokenObtainPairSerializer, APIRefreshTokenSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """
    JWT 토큰안의 payload에 추가적인 데이터 값을 삽입.
    """
    serializer_class = MyTokenObtainPairSerializer


class ApiRefreshRefreshTokenView(GenericAPIView):
    """
    토큰들을 모두 재발급
    """
    permission_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.
    authentication_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.

    serializer_class = APIRefreshTokenSerializer

    # 리프레시 토큰 자체를 다시 발급
    def post(self, request: HttpRequest):
        serializer: APIRefreshTokenSerializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        refresh: str = serializer.validated_data['refresh']

        try:
            refresh_token: RefreshToken = RefreshToken(refresh)
        except TokenError as e:
            raise InvalidToken(e)

        user: User = get_object_or_404(User, id=refresh_token['user_id'])
        new_refresh_token = MyTokenObtainPairSerializer.get_token(user)  # 이걸로 토큰을 생성해야 합니다. 다른 방법으로 하면 페이로드에 필수데이터가 누락된 버전이 생김
        new_access_token = new_refresh_token.access_token
        refresh_token.blacklist()  # 꼭 블랙리스트에 넣어주세요.

        return Response({
            'refresh': str(new_refresh_token),
            'access': str(new_access_token),
        })



class LoginAPI(viewsets.GenericViewSet):
    """
    로그인 View
    """

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = request.data.get('username')
        token = serializer.validated_data
        return Response(
            {
                'message': f'로그인 되었습니다. 반갑습니다 {user}님',
                'token': token
            }, status=status.HTTP_200_OK
        )
