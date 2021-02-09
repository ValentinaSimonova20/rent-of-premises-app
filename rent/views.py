from django.shortcuts import render
from django.http import HttpResponse

from .models import Premises


def index(request):
    premises = Premises.objects.all()
    context = {
        'premises': premises,
        'title': 'Офисы'
    }

    return render(request, template_name='rent/index.html', context=context)
