# server/chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer

def simple_bot_reply(user_text: str) -> str:
    text = user_text.strip().lower()
    if text in ("hi", "hello", "hey"):
        return "Hello! 👋 How can I help you today?"
    if "price" in text:
        return "I'm a demo bot: I can't fetch live prices yet, but you can ask me general questions!"
    if text.endswith("?"):
        return "Great question! (demo reply) Try asking about features or say 'help'."
    return "Noted! (demo reply). Ask me a question or say 'help' for tips."

class ChatListCreate(APIView):
    def get(self, request):
        messages = Message.objects.all()
        return Response(MessageSerializer(messages, many=True).data)

    def post(self, request):
        # Save user message
        serializer = MessageSerializer(data={'role': 'user', 'content': request.data.get('content', '')})
        serializer.is_valid(raise_exception=True)
        user_msg = serializer.save()

        # Bot reply
        bot_content = simple_bot_reply(user_msg.content)
        bot = Message.objects.create(role='bot', content=bot_content)

        return Response({
            'user': MessageSerializer(user_msg).data,
            'bot': MessageSerializer(bot).data
        }, status=status.HTTP_201_CREATED)
