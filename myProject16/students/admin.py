from django.contrib import admin
from .models import Student

@admin. register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('name', 'age')
    search_fields = ('name', 'city')
    list_filter = ('age', 'city')

    