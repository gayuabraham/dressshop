from .views import *
from django.urls import path

urlpatterns = [
    path('' , get_all_data),
    path('signup' , sigup_page , name='signup'),
    path('login/' , login_page , name = 'login'),
    path('signup_function', signup_function)
]
