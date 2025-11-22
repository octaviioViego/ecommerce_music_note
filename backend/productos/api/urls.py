from django.urls import path
from .views import ProductoAPIView

urlpatterns = [
    path('', ProductoAPIView.as_view(), name='producto'),
]
