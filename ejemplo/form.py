from ast import Pass
from django import forms
from .models import Comentario, ComentarioPosteo, GaleriaFoto, Noticia
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class comentarioForm(forms.ModelForm):
    class Meta: 
        model = Comentario
        # fields = ('dni','apellido','nombre','email','telefono','textoComentario',)
        fields = '__all__'

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','texto','imagen']
        # fields = '__all__'

class fotoForm(forms.ModelForm):
    class Meta:
        model = GaleriaFoto 
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = { k: '' for k in fields}


class ComentarPosteoForm(forms.ModelForm):
    class Meta:
        model = ComentarioPosteo
        fields = ['cuerpo']


               
