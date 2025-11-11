from django.db import models
class ChatMessage(models.Model):
    role = models.CharField(max_length=10)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
