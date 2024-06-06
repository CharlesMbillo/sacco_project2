from django.urls import path
from . import views
from .consumers import TransactionConsumer

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction/', views.transaction, name='transaction'),
    path('api/transactions/', views.TransactionList.as_view(), name='transactions'),
    path('ws/transactions/', TransactionConsumer.as_asgi(), name='ws_transactions'),
]