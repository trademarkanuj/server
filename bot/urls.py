from django.urls import path
from .views import index, ping, chat_view, chats_list
urlpatterns=[
    path('', index),
    path('api/ping', ping),
    path('api/chat', chat_view),
    path('api/chats', chats_list),
]
