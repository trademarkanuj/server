import os
import google.generativeai as genai
from django.conf import settings
key=settings.GOOGLE_API_KEY or os.getenv("GOOGLE_API_KEY","")
if key: genai.configure(api_key=key)
model_name=settings.DEFAULT_MODEL
class GeminiClient:
    def __init__(self, model=None):
        self.model=genai.GenerativeModel(model or model_name)
    def chat(self, message, system=None, history=None):
        response=self.model.generate_content([
            {"role":"user","parts":[{"text":message}]}
        ]+(history or []))
        return getattr(response,"text",str(response))
