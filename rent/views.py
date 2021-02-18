from django.shortcuts import render, redirect
from .forms import PremisesForm

from .models import Premises


def index(request):
    premises = Premises.objects.all()
    context = {
        'premises': premises,
        'title': 'Офисы'
    }

    return render(request, template_name='rent/index.html', context=context)


def image_upload_view(request):

    if request.method == 'POST':
        form = PremisesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PremisesForm()
    return render(request, 'rent/createPremises.html', {'form': form})

