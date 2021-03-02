from django.shortcuts import render
# from django.http import HttpResponse
from hello_django.calc.models import History
from django.views.generic.base import TemplateView


class Calc(TemplateView):
    template_name = 'calc.html'

    def get_context_data(self, a=0, b=0, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a'] = a
        context['b'] = b
        context['sum'] = a + b
        History(value=context['sum']).save()
        return context


def history(request):
    return render(request, 'history.html', context=History.objects.all())


def index(request, a=0, b=0):
    return render(request, 'calc.html', context={
        'result': a + b
    })
