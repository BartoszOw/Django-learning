from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome(request):
    return render(request, 'greetings/welcome.html')

def about(request):
    c= {'info1': 'Mam na imie Bartosz',
        'info2': 'Programuje w Python',
        'info3': 'Mieszkam w malym miescie',
        'info4': "Mam 6'2 wysokosci",
        'info5': "Jestem blondynem (takim ciemniejszym)",
        'active_page': 'bio'
        }
    return render(request, 'greetings/aboutpage.html', c)

def contact(request):
    return render(request, 'greetings/contactpage.html')