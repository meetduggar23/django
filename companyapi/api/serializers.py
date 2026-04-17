from rest_framework import serializers
from api.models import Company,Employee


class CompanySerializer(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'   # includes id + all fields

class EmployeeSerializer(serializers.ModelSerializer):
    Employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'

        def create(self, validated_data):
            return Employee.objects.create(**validated_data)

