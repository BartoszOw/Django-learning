from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib import messages
from maths.models import Math, Result
from maths.forms import ResultForm


# Create your views here.
def math(request):
    return HttpResponse('Tu Bedzie matma')
def add(request, a, b):
    res = a + b
    c = {'a': a, 'b': b, "operacja": '+', 'wynik': res, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=res)[0]
    Math.objects.create(operation='add',a=a,b=b, result=result)
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def sub(request, a, b):
    res = a - b
    c = {'a': a, 'b': b, "operacja": '-', 'wynik': res, "title": "odejmowanie"}

    result = Result.objects.get_or_create(value=res)[0]
    Math.objects.create(operation='sub',a=a,b=b, result=result)
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def mul(request, a, b):
    res = a * b
    c = {'a': a, 'b': b, "operacja": '*', 'wynik': res, "title": "mnożenie"}

    result = Result.objects.get_or_create(value=res)[0]
    Math.objects.create(operation='mul',a=a,b=b, result=result)
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))
def div(request, a, b):
    res = a / b
    c = {'a': a, 'b': b, "operacja": '/', 'wynik': res, "title": "dzielenie"}

    result = Result.objects.get_or_create(value=res)[0]
    Math.objects.create(operation='div',a=a,b=b, result=result)
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    return HttpResponse(render(
        request=request,
        template_name='maths/operation.html',
        context=c
    ))

def maths_list(request):
    maths = Math.objects.all()
    return render(
        request=request,
        template_name='maths/list.html',
        context={'maths': maths}
    )

def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name='maths/details.html',
        context={'math': math}
    )

def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)
        
        if form.is_valid():
            if form.cleaned_data['error'] == '':
                form.cleaned_data['errror'] = None
            Result.objects.get_or_create(form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name='maths/results.html',
        context={
            'results': results,
            'form': form
                 }
    )