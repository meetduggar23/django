from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    blogs = [
        {"title": "django basics", "is_featured": True, "author": "mohit bhai"},
        {"title": "django advanced", "is_featured": False, "author": ""},
        {"title": "django rest framework", "is_featured": False, "author": "meet bhai"},
    ]

    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_content": "<h1>Welcome to My Blog</h1>",
    }

    return render(request, 'blog/blog_list.html', context)
