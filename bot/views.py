import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .utils import GeminiClient

_S = {}   # in-memory storage


def index(req):
    return HttpResponse("<h1>Django Chatbot OK</h1>")


def ping(req):
    return JsonResponse({"ok": True, "model": settings.DEFAULT_MODEL})


@csrf_exempt
def chat_view(req):

    if req.method == "GET":
        return JsonResponse({"usage": "POST message"})

    if req.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # ✅ clean JSON load
    try:
        body = req.body.decode("utf-8") if req.body else "{}"
        data = json.loads(body)
    except:
        data = {}

    session_id = data.get("session_id", "default")
    message = data.get("message", "")

    if not message:
        return JsonResponse({"error": "message required"}, status=400)

    # ✅ ensure history is LIST
    raw_history = data.get("history", [])
    history = raw_history if isinstance(raw_history, list) else []

    # ✅ store user message
    _S.setdefault(session_id, []).append({"role": "user", "content": message})

    # ✅ call AI
    client = GeminiClient()

    try:
        reply = client.chat(message, history=history)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    # ✅ store bot reply
    _S[session_id].append({"role": "model", "content": reply})

    return JsonResponse({
        "session_id": session_id,
        "reply": reply,
        "messages": _S.get(session_id, [])
    })


def chats_list(req):
    sid = req.GET.get("session_id", "default")
    return JsonResponse({"messages": _S.get(sid, [])})
