from django.shortcuts import render, redirect
from .forms import PremisesForm

from .models import Premises, Applications
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


def by_area(request, area_id):
    current_area = Premises.objects.get(pk=area_id)
    context = {'current_area': current_area}

    return render(request, 'rent/by_area.html', context)


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


# отображение заявок пользователя
def get_apps(request):
    if request.user.is_staff:
        applications = Applications.objects.all()
    else:

        applications = Applications.objects.all().filter(client=request.user)
    context = {
        'apps': applications
    }

    return render(request, template_name='rent/applications.html', context=context)


# подать заявку на площадь
def add_app(request, area_id):
    current_area = Premises.objects.get(pk=area_id)
    new_app = Applications(client=request.user, premises=current_area, additionalInfo=request.POST['addInfo'])
    new_app.save()
    current_area = Premises.objects.get(pk=area_id)
    context = {'current_area': current_area}
    return render(request, 'rent/by_area.html', context)
