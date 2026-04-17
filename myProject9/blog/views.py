from django.shortcuts import render   # ✔ correct

def home(request):
    return render(request, 'base.html')

def blog(request):
    student =[
    {"name": "Meet", "age": 22, "city": "Ahmedabad"},
    {"name": "John", "age": 25, "city": "New York"},
    {"name": "Alice", "age": 30, "city": "Los Angeles"},
    {"name": "Bob", "age": 28, "city": "Chicago"},

]
    return render(request, 'blog.html', {'student': student})
