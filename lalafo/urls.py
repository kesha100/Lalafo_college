from django.urls import path, include
from .views import *


urlpatterns = [
    path('api/v1/product-info/<int:pk>', ProductListAPIView.as_view()),
    path('api/v1/product-info/', ProductListAPIView.as_view())
]