
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo', views.novo_topico_view, name='novo'),
    path('edita/<int:topico_id>', views.edita_topico_view, name='edita'),
    path('apaga/<int:topico_id>', views.apaga_topico_view, name='apaga'),
    path('quiz', views.quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('novoprojeto', views.novo_projeto_view, name='novoprojeto'),
    path('editarprojeto/<int:topico_id>', views.editar_projeto_view, name='editarprojeto'),
    path('apagarprojeto/<int:topico_id>', views.apagar_projeto_view, name='apagarprojeto'),
    path('novocadeira', views.novo_cadeira_view, name='novocadeira'),
    path('editarcadeira/<int:topico_id>', views.editar_cadeira_view, name='editarcadeira'),
    path('apagarcadeira/<int:topico_id>', views.apagar_cadeira_view, name='apagarcadeira'),
    path('', views.home_page_view, name='home'),
]