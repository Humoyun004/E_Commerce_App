from django.urls import path

from .views import Home, Message

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/<int:pk>', Message.as_view(), name='message'),
]