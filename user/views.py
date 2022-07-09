from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializers import LoginSerializer


# Create your views here.
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
