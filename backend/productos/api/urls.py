from django.urls import path
from .views import ProductoListCreateAPIView

urlpatterns = [
    path('', ProductoListCreateAPIView.as_view(), name='productos-list'),
]
