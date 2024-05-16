from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def math(request):
    return HttpResponse('Tu Bedzie matma')
def add(request, a, b):
    a,b = int(a), int(b)
    res = a + b
    c = {'a': a, 'b': b, "operacja": '+', 'wynik': res, "title": "dodawanie"}
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def sub(request, a, b):
    a,b = int(a), int(b)
    res = a - b
    c = {'a': a, 'b': b, "operacja": '-', 'wynik': res, "title": "odejmowanie"}
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def mul(request, a, b):
    a,b = int(a), int(b)
    res = a * b
    c = {'a': a, 'b': b, "operacja": '*', 'wynik': res, "title": "mnożenie"}
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def div(request, a, b):
    a,b = int(a), int(b)
    res = a / b
    c = {'a': a, 'b': b, "operacja": '/', 'wynik': res, "title": "dzielenie"}
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))