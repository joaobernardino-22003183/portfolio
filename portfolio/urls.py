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
    path('tfc', views.tfc_page_view, name='tfc'),
    path('novotfc', views.novo_tfc_view, name='novotfc'),
    path('editartfc/<int:topico_id>', views.editar_tfc_view, name='editartfc'),
    path('apagartfc/<int:topico_id>', views.apagar_tfc_view, name='apagartfc'),
    path('sobremim', views.sobremim_view, name='sobremim'),
    path('projetosgeral', views.projetos_geral_view, name='projetosgeral'),
    path('web', views.web_view, name='web'),
    path('tec', views.tec_view, name='tec'),
    path('labs', views.labs_view, name='labs'),
    path('sobreportfolio', views.sobre_portfolio_view, name='sobreportfolio'),
    path('contactos', views.contactos_view, name='contactos'),
    path('noticias', views.noticias_view, name='noticias'),
    path('', views.home_page_view, name='home'),
]