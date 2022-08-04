
from django.urls import path

from .views import ProductDetailsApiView

urlpatterns = [
    path('' , ProductDetailsApiView.as_view()),
    path('<int:pk>/' , ProductDetailsApiView.as_view()),
]

 
