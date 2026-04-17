from django.shortcuts import render
from datetime import datetime

class User:   # 👈 Capital U
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = { 
        "name": "meet duggar",
        "age": "20",
        "skill": ["python", "android studio", "editing", "writting", "scriptting"],
        "user": User("kumar", 30),   # ✅ Now correct
        "blog": {
            "title": "django template intro",
            "content": "<b>this is bold </b>",
            "created": datetime(2025,8,18,10,30)
        },
        "empty_value": None,
        
    }
    return render(request, "blog/home.html", context)
