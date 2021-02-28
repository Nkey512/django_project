from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View


def index(request, a=0, b=0):
    return render(request, 'calc.html', context={
        'result': a + b
    })
