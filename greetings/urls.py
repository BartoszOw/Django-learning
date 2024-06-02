from django.urls import path
from .views import welcome, AboutView, ContactView

app_name = 'greetings'
urlpatterns = [
    path('', welcome, name='welcome'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]