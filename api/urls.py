from django.urls import path

from .views import api_home

urlpatterns = [
    path('', api_home, name='home'),
    path('<int:pk>/', api_home, name='home'),
]
