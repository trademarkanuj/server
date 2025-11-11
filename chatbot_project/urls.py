from django.urls import path, include
urlpatterns=[path('',include('bot.urls')),path('api/',include('bot.urls'))]