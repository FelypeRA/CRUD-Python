from django.forms import ModelForm
from app.models import Pessoas

# Create the form class.
class PessoasForm(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome', 'email', 'telefone']