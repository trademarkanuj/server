import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
def home(request):
    return render(request, "index.html")

@csrf_exempt
def chat_api(request):
    required_key = getattr(settings, "g0L1ritGqF6LYpbcikIo9Lno4QARTo2rKs2UGJi0QD7l8I0Q23ja3eI2OhtYzS6vDW8", None)
    client_key = request.headers.get("X-API-KEY")

    if required_key and client_key != required_key:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    if request.method != "POST":
        return HttpResponseBadRequest('POST JSON: {"message": "..."}')

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    user_msg = (data.get("message") or "").strip()
    if not user_msg:
        return HttpResponseBadRequest("Field 'message' is required")

    bot_reply = f"You said: {user_msg}"
    return JsonResponse({"reply": bot_reply})
