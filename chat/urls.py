# server/chat/urls.py
from django.urls import path
from .views import ChatListCreate

urlpatterns = [
    path('messages/', ChatListCreate.as_view(), name='messages'),
]
