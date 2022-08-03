

from django.contrib import admin
from django.urls import include, path

from .views import ProductDetailsApiView

urlpatterns = [
    path('' , ProductDetailsApiView.as_view()),
    path('<int:pk>/' , ProductDetailsApiView.as_view()),
]

 
