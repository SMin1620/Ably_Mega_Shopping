from django.urls import path

from user.views import (
    LoginAPI,
    RegisterAPI,
)

app_name = 'user'

user_login = LoginAPI.as_view({
    'post': 'login'
})

user_register = RegisterAPI.as_view({
    'post': 'register'
})


urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
]