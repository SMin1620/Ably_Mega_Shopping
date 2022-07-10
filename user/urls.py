from django.urls import path

from user.views import (
    LoginAPI,
    RegisterAPI,
    UserDetailAPI,
)

app_name = 'user'

user_login = LoginAPI.as_view({
    'post': 'login'
})

user_register = RegisterAPI.as_view({
    'post': 'register'
})

user_detail = UserDetailAPI.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('<int:user_id>/', user_detail, name='user_detail'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
]