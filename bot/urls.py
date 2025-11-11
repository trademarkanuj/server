from django.urls import path
from .views import home,chat_api,get_all_chats
urlpatterns=[path('',home),path('chat',chat_api),path('chats',get_all_chats)]