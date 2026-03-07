from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Feedback


# =============================
# LOAD CHATBOT PAGE
# =============================

def home(request):
    return render(request, "index.html")


# =============================
# CHAT API (optional)
# =============================

@csrf_exempt
def chat(request):

    if request.method == "POST":

        data = json.loads(request.body)

        message = data.get("message", "")

        return JsonResponse({
            "answer": "Please choose one of the menu options."
        })


# =============================
# FEEDBACK API
# =============================

@csrf_exempt
def feedback(request):

    if request.method == "POST":

        try:

            data = json.loads(request.body)

            rating = data.get("rating")
            name = data.get("name")
            phone = data.get("phone")
            email = data.get("email")
            message = data.get("message")

            feedback = Feedback.objects.create(
                rating=rating,
                name=name,
                phone=phone,
                email=email,
                message=message
            )

            # Print in terminal
            print("\n===== USER FEEDBACK =====")
            print("Rating:", rating)
            print("Name:", name)
            print("Phone:", phone)
            print("Email:", email)
            print("Issue:", message)
            print("=========================\n")

            return JsonResponse({"status": "success"})

        except Exception as e:

            print("Feedback error:", e)

            return JsonResponse({"status": "error"})