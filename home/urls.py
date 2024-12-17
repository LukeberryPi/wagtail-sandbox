from django.urls import path
from .views import my_custom_view

urlpatterns = [
    path('my-custom-view/', my_custom_view, name='my_custom_view'),
]
