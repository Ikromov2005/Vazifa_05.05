from django.urls import path
from .views import user_login , register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]





    