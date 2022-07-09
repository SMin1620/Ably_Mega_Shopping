from django.urls import path

from user.views import LoginAPI


user_login = LoginAPI.as_view({
    'post': 'login'
})



urlpatterns = [
    path('login/', user_login, name='login'),
]