from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_info, name='phone_info'),
]
