from django.forms import ModelForm

from .models import Premises


class PremisesForm(ModelForm):
    class Meta:
        model = Premises
        fields = '__all__'
