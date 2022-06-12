from django import forms
from django.forms import ModelForm

from .models import Post
from .models import Projeto
from .models import Cadeira
from .models import TFC


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'assunto..'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'nome_autor': 'Nome',
            'descricao': 'Descrição'
        }

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'Nome_Projeto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'descricao': 'Descrição',
            'imagem' : 'Imagem'
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'ano': 'Ano',
            'ects' : 'ects'
        }

class TFCForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
        }

