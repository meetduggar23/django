from django.shortcuts import render
from datetime import datetime

def blog_detail(request):
    post = {
        "title": "My Second Blog Post",
        "content": "This is the content of my first blog post.",
        "author": "Yes",
        "created_at": datetime(2024, 6, 1, 12, 0, 0),
        "comments_count": 5,
        "tags": ["django", "python", "webdevelopment"],
        "price":15500,
        "number": 44,

    }
    return render(request, 'blog/blog_detail.html', {"post": post})
