from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def contact_form(request):
    return render(request, 'contact.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and message:
            Contact.objects.create(name=name, email=email, message=message)
            return HttpResponse(f"Thank you, {name}! for your message!")
        else:
            return HttpResponse("Please fill in all required fields.")

    return HttpResponse("contact_form")