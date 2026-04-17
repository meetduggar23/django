from django.http import HttpResponse


def home_page(request):
    print("Hello World")  # prints in terminal
    friends = ["Meet", "Duggar", "Sahil", "Shivam"]

    return HttpResponse(
        f"<h1>Hello World</h1><p>Friends: {', '.join(friends)}</p>"
    )