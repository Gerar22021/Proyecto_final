from django.contrib.auth.forms import UserCreationForm
from apps.blog_auth.models import Usuario
from apps.blog_auth.signals import Perfil

class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'password1',
            'password2'

        )