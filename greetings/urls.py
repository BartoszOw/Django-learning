from django.urls import path
from .views import greet, greet_to_u

urlpatterns = [
    path('', greet),
    path('<str:a>', greet_to_u)
]