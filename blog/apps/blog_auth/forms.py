from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.blog_auth.models import Usuario

class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )