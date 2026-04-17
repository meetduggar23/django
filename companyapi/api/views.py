from django.http import HttpResponse
from rest_framework import viewsets
from api.models import Company, Employee

from api.serializers import CompanySerializer, EmployeeSerializer


def home_page(request):
    return HttpResponse("<h1>Hello World</h1>")


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()