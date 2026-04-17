from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_msg,name='index'),
    path('success/',views.success,name='success'),
]