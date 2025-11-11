import json, requests
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from .models import ChatMessage

def add_cors(r):
    r['Access-Control-Allow-Origin']='*'
    r['Access-Control-Allow-Headers']='Content-Type,X-API-KEY'
    r['Access-Control-Allow-Methods']='GET,POST,OPTIONS'
    return r

def home(request):
    return render(request,"index.html")

def get_all_chats(request):
    data=list(ChatMessage.objects.values().order_by("timestamp"))
    return add_cors(JsonResponse(data,safe=False))

@csrf_exempt
def chat_api(request):
    if request.method=="OPTIONS":
        return add_cors(HttpResponse(status=204))
    required=settings.CHATBOT_API_KEY
    client=request.headers.get("X-API-KEY") or request.GET.get("key")
    if client!=required:
        return add_cors(JsonResponse({"error":"Unauthorized"},status=401))

    if request.method=="GET":
        msg=(request.GET.get("message") or "").strip()
        if not msg: return add_cors(HttpResponseBadRequest("message required"))
    else:
        try: data=json.loads(request.body)
        except: return add_cors(HttpResponseBadRequest("Invalid JSON"))
        msg=(data.get("message") or "").strip()
        if not msg: return add_cors(HttpResponseBadRequest("message required"))

    ChatMessage.objects.create(role="user",message=msg)
    reply=f"{msg}"
    ChatMessage.objects.create(role="bot", message=reply)
    return add_cors(JsonResponse([
    {
        "role": "bot",
        "message": reply
    }
], safe=False))
