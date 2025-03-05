from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('auth/', obtain_auth_token)
    
]