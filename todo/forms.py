from django.forms import ModelForm
from .models import Dolist


class InputForm(ModelForm):
    class Meta:
        model = Dolist
        fields = ('work',)
