from django.urls import path

from .views import logout_user, login_user, RegisterUser

app_name = 'users'
urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('register/', RegisterUser.as_view(extra_context={'title': 'Регистрация'}), name='register'),
]
