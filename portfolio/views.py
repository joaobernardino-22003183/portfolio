import matplotlib
import datetime

from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

from .models import Post
from .models import Projeto
from .models import Cadeira
from .models import PontuacaoQuizz
from .models import TFC

from .forms import PostForm
from .forms import ProjetoForm
from .forms import CadeiraForm
from .forms import TFCForm

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

matplotlib.use('Agg')


# Create your views here.
def home_page_view(request):
    agora = datetime.datetime.now()
    context = {
        'hora': agora.hour,
    }

    return render(request, 'portfolio/home.html', context)

def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)

def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def blog_page_view(request):
    context = {'portfolio': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def tfc_page_view(request):
    context = {'trabalhos': TFC.objects.all()}
    return render(request, 'portfolio/tfc.html', context)

def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontos=p)
        r.save()

    desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')

def pontuacao_quizz(request):
    pontuacao = 0
    if request.POST['primeira'] == "Cascading Style Sheets":
        pontuacao += 1

    if request.POST['segunda'] == "HyperText Markup Language":
        pontuacao += 1

    if request.POST['terceira'] == "Marcadores":
        pontuacao += 1

    if request.POST['quarta'] == "Estruturar o conteúdo de uma página web":
        pontuacao += 1

    if request.POST['quinta'] == "Estilizar o conteúdo da página web.":
        pontuacao += 1

    return pontuacao

def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontos, reverse=False)
    listaNomes = []
    listapontuacao = []

    for person in pontuacao_sorted:
        listaNomes.append(person.nome)
        listapontuacao.append(person.pontos)

    plt.barh(listaNomes, listapontuacao)
    plt.savefig('portfolio/static/portfolio/images/resultados.png', bbox_inches='tight')

def novo_topico_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/novo.html', context)

def edita_topico_view(request, topico_id):
    topico = Post.objects.get(id=topico_id)
    form = PostForm(request.POST or None, instance=topico)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'topico_id': topico_id}
    return render(request, 'portfolio/edita.html', context)

def apaga_topico_view(request, topico_id):
    Post.objects.get(id=topico_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}
    return render(request, 'portfolio/novo.html', context)

def editar_projeto_view(request, topico_id):
    topico = Projeto.objects.get(id=topico_id)
    form = ProjetoForm(request.POST or None, instance=topico)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'topico_id': topico_id}
    return render(request, 'portfolio/editar_projeto.html', context)

def apagar_projeto_view(request, topico_id):
    Projeto.objects.get(id=topico_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

def novo_cadeira_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}
    return render(request, 'portfolio/novo_cadeira.html', context)

def editar_cadeira_view(request, topico_id):
    topico = Cadeira.objects.get(id=topico_id)
    form = CadeiraForm(request.POST or None, instance=topico)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'topico_id': topico_id}
    return render(request, 'portfolio/editar_licenciatura.html', context)

def apagar_cadeira_view(request, topico_id):
    Cadeira.objects.get(id=topico_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))

def novo_tfc_view(request):
    form = TFCForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfc'))

    context = {'form': form}
    return render(request, 'portfolio/novo.html', context)

def editar_tfc_view(request, topico_id):
    topico = TFC.objects.get(id=topico_id)
    form = TFCForm(request.POST or None, instance=topico)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfc'))

    context = {'form': form, 'topico_id': topico_id}
    return render(request, 'portfolio/editar_tfc.html', context)

def apagar_tfc_view(request, topico_id):
    TFC.objects.get(id=topico_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tfc'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })

def sobremim_view(request):
    return render(request,'portfolio/sobremim.html')

def projetos_geral_view(request):
    return render(request,'portfolio/projetos_geral.html')

def web_view(request):
    return render(request,'portfolio/web.html')

def tec_view(request):
    return render(request,'portfolio/tec.html')

def labs_view(request):
    return render(request, 'portfolio/labs.html')

def sobre_portfolio_view(request):
    return render(request, 'portfolio/sobreportfolio.html')

def contactos_view(request):
    return render(request, 'portfolio/contactos.html')

def noticias_view(request):
    return render(request, 'portfolio/noticias.html')