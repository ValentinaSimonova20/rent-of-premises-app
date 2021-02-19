from django.shortcuts import render, redirect
from .forms import PremisesForm

from .models import Premises
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# вывод списка всех офисов
def index(request):
    premises = Premises.objects.all()
    context = {
        'premises': premises,
        'title': 'Офисы'
    }

    return render(request, template_name='rent/index.html', context=context)


# добавление офиса
def image_upload_view(request):
    if request.method == 'POST':
        form = PremisesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PremisesForm()
    return render(request, 'rent/createPremises.html', {'form': form})


# регистрация
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
