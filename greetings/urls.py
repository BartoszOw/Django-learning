from django.urls import path
from .views import about, contact, welcome

app_name = 'greetings'
urlpatterns = [
    path('', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]